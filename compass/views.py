from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category, Compass


def index(request,):
    return render(request, 'index.html', {"categories":  Category.all()})


def categories(request,):
    return render(request, 'categories.html', {
        "categories": Category.all(),
    })


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'category.html', {
        "category": category,
        "categories": Category.all(),
        "books": Compass.find(category=category)
    })


def book(request, book_slug):
    return render(request, 'book.html', {
        "book":   get_object_or_404(Book, slug=book_slug),
        "categories": Category.all(),
        })


def search(request):
    if (request.method == 'GET'):
        return redirect('/')

    if(request.method == 'POST'):
        title = request.POST.get('title')
        category = request.POST.get('category')
        books = Compass.find(
            title=title,
            category=category)

        return render(
            request,
            'books.html', {
                "books": books,
                "title": Compass.heading(title=title, category=category),
                "categories": Category.all(),
             })
