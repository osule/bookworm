from django.test import TestCase
from compass.models import (Category,
                            Book)


class CategoryTestCase(TestCase):
    def test_can_add_category(self,):
        Category.create(title="Mock Category")
        self.assertEqual(Category.find("Mock Category").count(), 1)


class BookTestCase(TestCase):
    def test_can_add_book(self):
        category = Category.create(title="Mock Category")
        Book.create(title="Mock Book", category=category)
        self.assertEqual(Book.find("Mock Book").count(), 1)
