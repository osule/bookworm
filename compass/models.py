from datetime import datetime
from django.db import models
from .utils import slugify_with_date_now


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def create(cls, title):
        now = datetime.now()
        return cls.objects.create(title=title,
                                  slug=slugify_with_date_now(title, now))

    @classmethod
    def find(cls, title):
        return cls.objects.filter(title=title)

    def __str__(self):
        return "{}".format(self.title,)


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    category = models.ForeignKey(Category)

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def create(cls, title, category,):
        now = datetime.now()
        return cls.objects.create(title=title,
                                  slug=slugify_with_date_now(title, now),
                                  category=category)

    @classmethod
    def find(cls, title=None, category=None,):
        if title and not category:
            return cls.objects.filter(title=title,)
        if category and not title:
            return cls.objects.filter(category=category,)
        return cls.objects.filter(title=title, category=category)


class Compass(object):
    @classmethod
    def find(cls, **kwargs):
        title = kwargs.get('title')
        category = kwargs.get('category')
        if not title and not category:
            return Book.all()
        if not title:
            return Book.find(category=Category.find(title=category))
        if not category:
            return Book.find(title=title)

    @classmethod
    def heading(cls, **kwargs):
        title = kwargs.get('title')
        category = kwargs.get('category')
        if not title and not category:
            return "All books"
        if not title:
            return "All book titles under {}".format(category)
        if not category:
            return "All book titles like {}".format(title)
        return "All books like {} under {}".format(title, category)
