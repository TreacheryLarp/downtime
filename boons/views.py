from django.shortcuts import render

def transaction(request, boon):
    return render(request, 'transaction.html', {'boon': boon})
