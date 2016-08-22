from django.test import TestCase
from compass.models import (Category,
                            Book, Compass)


class CategoryTestCase(TestCase):
    def test_can_add_category(self,):
        Category.create(title="Mock Category")
        self.assertEqual(Category.find("Mock Category").count(), 1)


class BookTestCase(TestCase):
    def test_can_add_book(self):
        category = Category.create(title="Mock Category")
        Book.create(title="Mock Book", category=category)
        self.assertEqual(Book.find("Mock Book").count(), 1)


class CompassTestCase(TestCase):
    def test_correct_title_if_title_and_category(self,):
        heading = Compass.heading(title="Title 1", category="Category 1")
        self.assertEqual(heading, "All books like Title 1 under Category 1")

    def test_correct_title_if_not_title_and_category(self,):
        heading = Compass.heading(title="", category="")
        self.assertEqual(heading, "All books")

    def test_correct_title_if_not_category(self,):
        heading = Compass.heading(title="Title 1", category="")
        self.assertEqual(heading, "All book titles like Title 1")

    def test_correct_title_if_not_title(self,):
        heading = Compass.heading(title="", category="Category 1")
        self.assertEqual(heading, "All book titles under Category 1")
