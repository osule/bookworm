from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='category_master'),
    path('categories/<slug:category_slug>/',
        views.category, name='category_detail'),
    path('books/(<slug:book_slug>/',
        views.book, name='book_detail'),
    path('search/',
        views.search, name='compass_find')
]
