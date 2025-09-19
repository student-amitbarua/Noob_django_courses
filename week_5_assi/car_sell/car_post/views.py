from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .import forms 
from . import models
from django.utils.decorators import method_decorator 
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

@login_required
def add_post(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            car_form.instance.owner = request.user
            car_form.save()
            return redirect('car_post')
        
    else:
        car_form = forms.CarForm()
        return render(request, 'car_post.html', {'form' : car_form})
    

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'car_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

@login_required
def delete_post(request, id):
    car=models.Car.objects.get(pk=id)
    car.delete()
    return redirect('homepage')

class DetailPostView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = "post_details.html"

    def car(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


    

    

