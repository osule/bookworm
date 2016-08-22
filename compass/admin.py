from django.contrib import admin
from .models import Book, Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category

    class Meta:
        verbose_name_plural = 'Categories'


admin.site.register(Book)
admin.site.register(Category, CategoryAdmin)
