from django.test import TestCase, Client
from ..models import Category, Book


class CompassTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Client()
        super(CompassTest, cls).setUpClass()

    def test_can_view_search_page(self):
        response = self.client.get('/')
        self.assertContains(response, '<input name="title" type="text"')

    def test_can_view_categories_page(self):
        response = self.client.get('/categories')
        self.assertContains(response, 'Categories')

    def test_can_view_category_page(self):
        Category.create(title="Category 1")
        response = self.client.get('/categories/category-1-2016-08-22')
        self.assertContains(response, 'Category 1')

    def test_can_view_book_page(self):
        category = Category.create(title="Mock Category")
        Book.create(title="Book 1", category=category)
        response = self.client.get(
            '/books/book-1-2016-08-22')
        self.assertContains(response, 'Book 1')

    def test_can_search_book_using_category_and_title(self):
        category = Category.create(title="Mock Category")
        Book.create(title="Book 1", category=category)

        response = self.client.post('/search', {
                "title": "Book 1",
                "category": "Mock category",
            })

        self.assertContains(
            response,
            'All books like Book 1 under Mock category')

    def test_can_search_book_using_only_title(self):
        category = Category.create(title="Mock Category")
        Book.create(title="Mock book", category=category)
        response = self.client.post('/search', {
                "title": "Mock book",
                "category": "",
            })
        self.assertContains(response, 'All book titles like Mock book')

    def test_can_search_using_only_category(self):
        category = Category.create(title="Mock Category")
        Book.create(title="Mock book", category=category)
        response = self.client.post('/search', {
                "title": "",
                "category": "Mock Category",
            })
        self.assertContains(response, 'All book titles under Mock Category')
