from django.shortcuts import render
from task_app.models import Task_app
from task_category.models import TaskCatagory
def home(request):

    data = Task_app.objects.all()
    info = TaskCatagory.objects.all()

    return render(request, 'home.html', {'data' : data, 'info' : info})