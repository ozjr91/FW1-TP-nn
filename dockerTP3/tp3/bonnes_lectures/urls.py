from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome,name='welcome'),
    path('book/',views.all_books,name='all_books'),
    path('book/<int:book_id>/',views.details, name='details'),
    path('new_book/', views.add_book, name='add_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
]
