from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import todoform
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import todo
# Create your views here.

@login_required(login_url='login/')
def index(request):
    
    if request.method == 'POST':
        Users = User.objects.get(username=request.user)
        kegiatan = request.POST['kegiatan']
        if kegiatan: 
            todo.objects.create(kegiatan = kegiatan,peserta=Users)
            messages.info(request, 'Create task succesful')
            return redirect('todo_app:index')
            
    myTodo = todo.objects.filter(peserta=request.user)
    # complite = todo.objects.filter(kegiatan)

    context = {
        'mytodo' : myTodo,
        # 'task' : complite,
    }

    return render(request, 'index.html', context)

def delete(request, delete_id):
    todo.objects.filter(id=delete_id).delete()
    return redirect('todo_app:index')

def masuk(request):
    if request.method == 'POST':
        username_login = request.POST['username']
        password_login = request.POST['password']
        User = authenticate(request, username=username_login, password=password_login)
        

        if User is not None:
            login(request,User)
            messages.info(request,'Login succesfully')
            return redirect('todo_app:index')
        # elif User wro

        else:
            messages.info(request,'Login failed, check email or password ')
            return redirect('todo_app:login')

    elif request.user.is_authenticated:
            return redirect('todo_app:index')
    else :
        return render(request,'login.html')

def keluar(request):
    logout(request)
    return redirect('todo_app:login')


def daftar(request):
    forms = UserCreationForm(request.POST)
    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return redirect('todo_app:index')
            
        else :
            return redirect('todo_app:register')      
    
    else :
        return render(request,'register.html', {'form':forms} )
@login_required
def buat(request):
    form = todoform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('todo_app:index')
    else:
        return render(request,'register2.html',{'form': form})
# def register(request):
#     form  = RegisterForm(request.POST)
#     if request.method == 'POST':
        
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + user)
#             return redirect('todo_app:login')
#         else :
#             return redirect('todo_app:daftar')

#     # elif request.user.is_authenticated:
#     #     return redirect('todo_app:index')
    
#     return render(request, 'register2.html', {'form': form})

   

   