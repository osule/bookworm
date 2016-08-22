from django.test import TestCase, Client
from ..models import Category, Book



class CompassTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Client()
        super(CompassTest, cls).setUpClass()

    def test_can_view_search_page(self):
        response = self.client.get('/')
        self.assertContains(response, '<input name="title" type="text"/>')

    def test_can_view_categories_page(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Book Categories</title>')

    def test_can_view_books_page(self):
        response = self.client.get('/categories/')
        self.assertContains(response, '<title>Book Categories</title>')

    def test_can_view_category_page(self):
        Category.create(title="Mock Category")
        response = self.client.get('/categories/mock-category-2016-08-22')
        self.assertContains(response, '<title>Mock Category</title>')

    def test_can_view_book_page(self):
        category = Category.create(title="Mock Category")
        Book.create(title="Mock book", category=category)
        response = self.client.get(
            '/categories/mock-category-2016-08-22/books/mock-book-2016-08-22')
        self.assertContains(response, '<title>Mock Book</title>')

    def test_can_search_book_using_category_and_title(self):
        category = Category.create(title="Mock Category")
        Book.create(title="Mock book", category=category)

        response = self.client.post('/search', {
                "title": "Mock book",
                "category": "Mock category",
            })

        self.assertContains(response, 'Mock book')

    def test_can_search_book_using_only_title(self):
        category = Category.create(title="Mock Category")
        Book.create(title="Mock book", category=category)
        response = self.client.post('/search', {
                "title": "Mock book",
                "category": "",
            })
        self.assertContains(response, 'Mock book')

    def test_can_search_using_only_category(self):
        category = Category.create(title="Mock Category")
        Book.create(title="Mock book", category=category)
        response = self.client.post('/search', {
                "title": "",
                "category": "Mock Category",
            })
        self.assertContains(response, 'Mock book')
