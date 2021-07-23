from django.contrib import admin
from django import forms
from .models import Post, Category
from django_ckeditor_5.fields import CKEditor5Widget


class PostAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditor5Widget)
    class Meta:
        model = Post

    list_display = ['category', 'title', 'created_at']


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

    list_display = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)