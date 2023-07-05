from django.shortcuts import render, HttpResponse
from .models import ToDo



def index(request):
    to_do_list = ToDo.objects.all()
    return render(request, 'app/index.html', {'to_do_list': to_do_list})
