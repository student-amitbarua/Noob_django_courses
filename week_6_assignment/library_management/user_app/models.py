from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    balance_after_transaction = models.DecimalField(max_digits=15, decimal_places=3, default=0)  
    money = models.IntegerField(default=0)
    profession = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)


    def deposite(self, money):
        self.balance += money
        self.balance_after_transaction = self.balance
        self.save()

    def __str__(self):
        return f" profile of {self.user.username}"