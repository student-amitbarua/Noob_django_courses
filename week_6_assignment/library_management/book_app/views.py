from django.shortcuts import render
from .models import BookModel, BorrowBookModel, ReviewModel
from categories.models import CategoryModel
from django.views.generic import DetailView, UpdateView
from django.contrib import messages
from .forms import ReviewForm
# from user_app.views import send_user_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_list_or_404


# Create your views here.

def home (request, category_slug=None):
    book = BookModel.objects.all()
    if category_slug is not None:
        category = CategoryModel.objects.get(slug=category_slug)
        book = BookModel.objects.filter(category = category)
        

    category = CategoryModel.objects.all()
    return render(request, 'home.html', {'book':book, 'category':category})


class BookDetailView(DetailView):
    model = BookModel
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'
    context_object_name = 'book'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['reviews'] = ReviewModel.objects.filter(book=book)

        return context





@login_required
def BorrowingBook(request,id):
    book = BookModel.objects.get(pk=id)
    user = request.user.account
    if request.method == 'POST':
        copies = 1
        if copies <= book.copies and user.balance >= book.borrow_price:
            BorrowBookModel.objects.create(user= request.user, book=book, copies=copies)
            book.copies -= copies
            book.save()
            user.balance -= book.borrow_price
            user.save(
                update_fields = ['balance']

            )
            user.balance_after_transaction = user.balance 
            user.save(update_fields=['balance_after_transaction'])

            # send_user_mail(request, 'borrowing Book', 'borrowing_mail.html', book.borrow_price)

            messages.success(request, 'Borrow book successfull')
            return redirect('book_details', id = book.id)
        else:
            messages.error(request, 'you have not enough money to buy this book')

    return render(request, 'book_details.html', {'book':book})
    

@login_required
def AddReview(request, id):
    book= BookModel.objects.get(pk=id)
    user = request.user
    borrow_book = BorrowBookModel.objects.filter(user=user, book = book)

    if not borrow_book.exists():
        messages.error(request, 'At first you should take the book. Then you can review for this Book')
        return redirect('book_details', id=id)
    
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit= False)
            review.user = user
            review.book = book
            review.save()
            messages.success(request, 'you review has been submitted')
            return redirect('book_details', id=id)
        
        else:
            form = ReviewForm()

    return render(request, 'review_form.html', {'form':form, 'book':book})
    

@login_required
def  book_return(request, borrow_id):
    borrow_instance = get_list_or_404(BorrowBookModel, pk=borrow_id)
    user_account = request.user.account

    user_account.balance += borrow_instance.book.borrow_price
    user_account.save(update_fields=['balance'])

    borrow_instance.delete()

    # send_user_mail(request.user, 'Return Book', 'return_mail.html', borrow_instance.book.borrow_price)
    # messages.success(request, 'Book Return Successfull')

    return redirect('profile')