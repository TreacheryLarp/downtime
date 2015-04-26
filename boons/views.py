from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import CreateView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse

from boons.models import *

@login_required
def my_boons(request):
    debits = request.user.character.debits
    credits = request.user.character.credits
    return render(request, 'myboons.html', {'debits': debits, 'credits': credits})


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
