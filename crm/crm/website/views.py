from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpForm, AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.order_by('-id')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.success(request, 'Please try again')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form = SingUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('/')
        
    else:
        form = SingUpForm()

    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id = pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        # messages.success("You must be logged in...")
        return redirect('home')

    
def delete_record(request, pk):
    if request.user.is_authenticated:       
        delete_it = Record.objects.get(id = pk)
        delete_it.delete()
        return redirect('home')
    else:
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                # messages.success(request, "Add")
                return redirect('home')
            
        
        return render(request, 'add_record.html', {'form':form})
    else:
        return redirect('home')
    
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        return redirect('home')