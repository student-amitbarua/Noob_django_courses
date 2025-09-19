from django.shortcuts import render,redirect
from .import forms 
# Create your views here.

def add_brand(request):
    if request.method == 'POST':
        brand_form = forms.BrandFrom(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            return redirect('add_brand')
        
    else:
        brand_form = forms.BrandFrom()
    return render(request, 'add_brand.html', {'from': brand_form})
    
