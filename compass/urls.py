from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories$', views.categories, name='category_master'),
    url(r'^categories/(?P<category_slug>[\w-]+)$',
        views.category, name='category_detail'),
    url(r'^books/(?P<book_slug>[\w-]+)$',
        views.book, name='book_detail'),
    url(r'^search$',
        views.search, name='compass_find')
]
