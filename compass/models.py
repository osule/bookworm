from datetime import datetime
from django.db import models
from .utils import slugify_with_date_now


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    @classmethod
    def create(cls, title):
        now = datetime.now()
        return cls.objects.create(title=title,
                                  slug=slugify_with_date_now(title, now))

    @classmethod
    def find(cls, keyword):
        return cls.objects.filter(title=keyword)


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    category = models.ForeignKey(Category)

    @classmethod
    def create(cls, title, category):
        now = datetime.now()
        return cls.objects.create(title=title,
                                  slug=slugify_with_date_now(title, now),
                                  category=category)

    @classmethod
    def find(cls, keyword):
        return cls.objects.filter(title=keyword)


class Compass(object):
    @classmethod
    def delegate(cls,):
        pass
