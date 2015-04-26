from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import CreateView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse

from boons.models import *

@login_required
def transaction(request, boon_key):
    boon = get_object_or_404(Boon, pk=boon_key)

    if request.user.is_staff:
        data = {'boon': boon}

        if request.user.is_staff:
            if boon.is_activated:
                return BoonTransfer.as_view()(request, **data)
            else:
                boon.is_activated = True
                boon.save()
                return render(request, 'activated.html', data)
        else:
            redirect('boons.views.view_boon', boon_key=boon_key)

@login_required
def view_boon(request, boon_key):
    boon = get_object_or_404(Boon, pk=boon_key)
    user = request.user
    if (user.is_staff or boon.debtor == user.character or
        boon.creditor() == user.character):
        return render(request, 'boon.html', {'boon': boon})
    else:
        raise PermissionDenied

@login_required
def print_boon(request, boon_key):
    if not request.user.is_staff:
        raise PermissionDenied

    boon = get_object_or_404(Boon, pk=boon_key)
    url = request.build_absolute_uri(reverse('boons.views.transaction',
                                             kwargs={'boon_key' :boon_key}))
    return render(request, 'print.html', {'boon': boon, 'url': url})


# Only called by transfer and as such doesn't need any decorators.
class BoonTransfer(CreateView):
    model = Transaction
    fields = ['creditor']
    template_name = 'transfer.html'

    def get_initial(self):
        return {
            'creditor': self.kwargs['boon'].creditor,
        }

    def get_success_url(self):
        return reverse('boons.views.view_boon',
                        kwargs={'boon_key': self.kwargs['boon'].key})

    def get_context_data(self, **kwargs):
        context = super(BoonTransfer, self).get_context_data(**kwargs)
        context['boon'] = self.kwargs['boon']
        return context

    def form_valid(self, form):
        boon = self.kwargs['boon']
        form.instance.boon = boon
        ret = super(BoonTransfer, self).form_valid(form)
        boon.active_transaction = self.object
        boon.save()
        return ret
