from django.shortcuts import render , redirect
from .import forms
# Create your views here.

def add_category(request):
   if request.method == 'POST': #user post request korche
      category_form = forms.CategoryForm(request.POST)#user er post request data ekhane capture korlam
      if category_form.is_valid(): #post kora data gula amra valid kina check korchi
         category_form.save() # jodi data valid hoy taile database e save korvo
         return redirect('add_category')# sob thik takle takee add category te pathiye dibo
     
   else: #user narmally website e gele blank form pabe
      category_form = forms.CategoryForm()


   return render(request, 'add_category.html', {'form' : category_form})