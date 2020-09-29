from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    Tasks = task.objects.all()

    form = taskForm()
    if request.method == 'POST':
        form=taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': Tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def update_task(request, pk):
    Tasks=task.objects.get(id=pk) #Each link will of update will have different id

    form=taskForm(instance=Tasks) #Instacne prefills the form for us
    if request.method == 'POST':
        form=taskForm(request.POST, instance=Tasks)
         #IF its only request.POST without instance, then new tasks will be created while old ones remains
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'form':form}
    return render(request, 'tasks/update_task.html',context)

def delete(request, pk):
    item=task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect("/")
    context={'item': item}
    return render(request, 'tasks/delete_msg.html',context)
