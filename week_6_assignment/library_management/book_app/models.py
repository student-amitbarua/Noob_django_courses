from django.db import models
from categories.models import CategoryModel

from django.contrib.auth.models import User
# Create your models here.


class BookModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name= 'category')

    title = models.CharField(max_length=140)
    description = models.TextField()
    borrow_price = models.DecimalField(max_digits=12, decimal_places=3)
    image = models.ImageField(upload_to='book_app/media/uploads/', blank=True, null=True)
    copies = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return self.title
    

class BorrowBookModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowing')
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name= 'borrowing')
    copies = models.PositiveIntegerField()
    borrow_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    


class ReviewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=80)
    review_area = models.TextField()
    rating = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)