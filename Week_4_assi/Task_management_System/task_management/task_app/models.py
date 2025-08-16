from django.db import models

# Create your models here.

class Task_app(models.Model):

    task_Title = models.CharField(max_length=200)
    task_Description = models.TextField()
    is_completed = models.BooleanField(default = False)
    Task_Assign_Date = models.DateField()

    def __str__(self):
        return self.task_Title
