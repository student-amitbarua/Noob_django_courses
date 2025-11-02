from django.urls import path
from .import views 
from .views import BookDetailView

urlpatterns = [
    path('', views.home, name='homepage' ),
    path('categories/<slug:category_slug>/', views.home, name='Category_wise_book'),
    path('borrow_book/<int:id>/', views.BorrowingBook, name='borrow_book'),
    path('book_details/<int:id>/', BookDetailView.as_view(), name='book_details'),
    path('add_review/<int:id>', views.AddReview, name='book_review'),
    path('return_book/<int:borrow_id>', views.book_return, name='return_book')

]