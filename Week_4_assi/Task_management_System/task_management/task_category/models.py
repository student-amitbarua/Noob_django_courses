from django.db import models
from task_app.models import Task_app

# Create your models here.

class TaskCatagory(models.Model):
    CategoryName = models.CharField(max_length=70)
    tasks = models.ManyToManyField(Task_app)

    def __str__(self):
        return self.CategoryName