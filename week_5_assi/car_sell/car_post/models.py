from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_post/media/uploads/', blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.model
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name= 'comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f" comments by {self.user}"