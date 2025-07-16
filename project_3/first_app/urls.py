from django.urls import path
# from views import contact  # This line is commented out and potentially problematic
from . import views         # This line is correct for importing all views

urlpatterns = [
   
    path("courses/",views.courses),
    path("about/", views.about),
    path("", views.home),
    
]