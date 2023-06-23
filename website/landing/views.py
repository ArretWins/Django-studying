from django.shortcuts import render, HttpResponse
from .forms import SubscriberForm

def landing(request):
    name = 'Артём'
    form = SubscriberForm(request.POST or None)
    if request.method == "POST":
        form.save()
    return render(request, 'landing/landing.html', locals())
    # return HttpResponse('TEXT TUT')