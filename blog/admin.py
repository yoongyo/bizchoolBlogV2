from django.contrib import admin
from django import forms
from .models import Post, Category
from ckeditor.widgets import CKEditorWidget


class PostAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = Post

    list_display = ['category', 'title', 'created_at']


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

    list_display = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)