from ast import ExtSlice
from re import L
from turtle import title
from django.shortcuts import render, redirect
from .models import Todo 
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm
# Create your views here.

def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'todos':all})


def say_hello(request):
    person = {'name':'admin'}
    return render(request, 'hello.html', context=person)


def detail(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'detail.html', {'todo':todo})


def delete(request, id): #Delete Todo Task
    Todo.objects.get(id=id).delete()

    #Show success message 
    messages.success(request, 'Success Delete!', 'Success')
    return redirect('home')


def create(request): #create Todo Task

    if request.method == 'POST':
        form = TodoCreateForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
		#Send Todo Task Data To CleanData	
            Todo.objects.create(
                title=cd['title'],
                body=cd['body'],
                created=cd['created'])

            messages.success(request, 'Todo Created', 'success')
            return redirect('home')

    else:
        form = TodoCreateForm()

    return render(request, 'create.html', {'form':form})


def update(request, id): #update Todo Task
    
    #SHow Previous Date in forms 1
    todo = Todo.objects.get(id=id) #Create Todo Task link With id

	#Check Request Method
    if request.method == 'POST': 

        #Updaet Date in DataBase
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Your Todo Update Success', 'success')
            return redirect('details', id)

    else:
        #SHow Previous Date in forms 2
        form = TodoUpdateForm(instance=todo)

    return render(request, 'update.html', {'form':form})
