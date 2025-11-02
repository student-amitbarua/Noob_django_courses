from django.shortcuts import render

# Create your views here.

from .forms import RegistrationForm , DepositeForm, ProfileUpdateForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import FormView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from django.contrib.auth import login, logout
from .models import UserProfile, User
from  book_app.models import BorrowBookModel
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



# def send_user_mail(user, sub, template, money):
#     to_mail= user.email
#     message = render_to_string(template,{
#         'user' : user,
#         'money' : money,
#     })

#     sent_mail = EmailMultiAlternatives(sub,
#                                        body=message,
#                                          to=[to_mail])
#     sent_mail.attach_alternative(message, 'text/html')
#     sent_mail.send()



@login_required

def profile(request):
    user = request.user

    user_account, created = UserProfile.objects.get_or_create(
        user=user,
        defaults={
            'balance': 0.00,
            'balance_after_transacton': 0,
            'money': 0,
        }
    )
        
    borrow_books = BorrowBookModel.objects.filter(user=user)

    context = {
        'user_account': user_account,
        'borrow_books': borrow_books
    }
    return render(request, 'user_app/profile.html', context)




class UserRegistrationView(FormView):
    template_name = 'user_app/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
       user = form.save()
       return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'user_app/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


def User_logout(request):
    logout(request)
    return redirect('homepage')


@login_required

# def Deposite(request):
#     user_account, created = UserProfile.objects.get_or_create(user = request.user)
#     if request.method == 'POST':
#         user_account = request.user.account

#         form = DepositeForm(request.POST)

#         if form.is_valid():
#             money = form.cleaned_data['money']
#             user_account = request.user.account
#             user_account.deposite(money)

#             send_user_mail(request.user, 'Deposite successfull', 'user_app/deposite_mail.html', money)

#             return redirect('profile')
        
#     else:
#         form = DepositeForm()
#         return render(request, 'user_app/deposite.html', {'form':form})



def Deposite(request):
    # FIX 5: Remove this redundant get_or_create call. UserProfile is guaranteed 
    # to exist (or will be created) in the profile view or during registration 
    # if you set up signals. Keeping it simple here.
    # user_account, created = UserProfile.objects.get_or_create(user=request.user) 
    
    # We can just access it directly, assuming the profile() view ensures it exists.
    user_account = request.user.account 
    
    if request.method == 'POST':
        form = DepositeForm(request.POST)

        if form.is_valid():
            money = form.cleaned_data['money']
            
            # FIX 6: Use the deposite method on the fetched account
            user_account.deposite(money) 
            
            # FIX 7: Use f-string for clarity in the success message
            messages.success(request, f'Successfully deposited ${money}!')
            

            return redirect('profile')
        
    else:
        form = DepositeForm()
        
    return render(request, 'user_app/deposite.html', {'form': form})





class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    pk_url_kwarg = 'id'

    template_name = 'user_app/update_profile.html'
    success_url = reverse_lazy ('profile')

    def form_valid(self, form):
        update_form = super().form_valid(form)
        messages.success(self.request, 'profile update  successfull.')

        return update_form
    
class UserPassChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user_app/update_profile.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        pass_form = super().form_valid(form)
        messages.success(self.request, 'your password change successfully')
        return pass_form
    


    