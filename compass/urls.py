from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/$', views.index, name='index'),
    url(r'^/categories$', views.categories, name='category:master'),
    url(r'^/categories/(?P<category_slug>\w+)$',
        views.category, name='category:detail'),
    url(r'^/categories/(?P<category_slug>\w+)/books/(?P<book_slug>\w+)$',
        views.book, name='book:detail'),
    url(r'^/search$',
        views.search, name='compass:find')
]
