from django.shortcuts import render

from hello_world.models import workers


def hello(request):
    
    # new_worker = workers(age='Николай', surname = 'Наумов', salary = 12000)
    # new_worker.save()
    # workers.objects.get(id = 6).delete()
    all_workers = workers.objects.all()
    
    # for i in all_workers:
    #     print(f'Имя:{i.age} Фамилия:{i.surname} Зарплата:{i.salary} id:{i.id}')
    
    return render(request, 'index.html', context={'model': all_workers})