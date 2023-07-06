from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from django.views.decorators.http import require_http_methods



def index(request):
    to_do_list = ToDo.objects.order_by('-id')
    return render(request, 'app/index.html', {'to_do_list': to_do_list})


@require_http_methods(['POST'])
def add_todo(request):
    title = request.POST['title']
    note = request.POST['note']
    todo = ToDo(title=title, note=note)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id = todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id = todo_id)
    todo.delete()
    return redirect('index')