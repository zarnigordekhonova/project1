from django.urls import path
from books.views import get_book_name


urlpatterns = [
    path('', get_book_name)
]