import unittest
from compass.utils import slugify, slugify_with_date_now
from datetime import datetime


class UtilsTest(unittest.TestCase):
    def test_can_slugify_title(self):
        slug = slugify('Mock title')
        self.assertEqual(slug, 'mock-title')

    def test_can_slugify_with_date_now(self):
        now = datetime.now()
        slug_with_date_now = slugify_with_date_now('Mock title', now)
        self.assertEqual(slug_with_date_now, 'mock-title-2016-08-22')
