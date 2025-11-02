from django.urls import path
from .views import UserRegistrationView, UserLoginView, ProfileUpdate, UserPassChangeView
from .import views

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register' ),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.User_logout, name='logout'),
    path('login', views.profile, name='profile'),
    path('deposite/', views.Deposite, name='deposit'),
    path('update_profile/<int:id>/', ProfileUpdate.as_view(), name='update_profile'),
    path('password_change', UserPassChangeView.as_view(), name='pass_change'),
]
