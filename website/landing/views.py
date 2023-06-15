from django.shortcuts import render, HttpResponse


def landing(request):
    name = 'Артём'
    return render(request, 'landing/landing.html', locals())
    # return HttpResponse('TEXT TUT')