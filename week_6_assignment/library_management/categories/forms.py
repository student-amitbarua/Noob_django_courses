from .models import CategoryModel
from django import forms 

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        firelds= ['name', 'slug']