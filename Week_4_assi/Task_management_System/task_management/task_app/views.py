from django.shortcuts import render, redirect
from . import forms 
from . import models 

# Create your views here.

def add_task(request):
    if request.method == 'POST':
        task_app_form = forms.Task_appForm(request.POST)
        if task_app_form.is_valid():
            task_app_form.save()
            return redirect('add_task')
        
    else: 
        task_app_form = forms.Task_appForm()

    return render(request, 'add_task.html', {'form' : task_app_form})
    

def edit_task(request, id):
    task = models.Task_app.objects.get(pk=id)
    task_app_form = forms.Task_appForm(instance=task)
    if request.method == 'POST':
       task_app_form = forms.Task_appForm(request.POST, instance=task)

       if task_app_form.is_valid():
            task_app_form.save()

       return redirect ('homepage')
    return render(request, 'add_task.html', {"form" : task_app_form})


def delete_task(request, id):
    task = models.Task_app.objects.get(pk = id)
    task.delete()
    return redirect('homepage')