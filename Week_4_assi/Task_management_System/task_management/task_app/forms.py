from django import forms 
from .models import Task_app

class Task_appForm(forms.ModelForm):
    class Meta :
        model = Task_app
        fields = '__all__'
    