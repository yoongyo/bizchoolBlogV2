from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    content = CKEditor5Field(blank=True, null=True, config_name='extends')
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
