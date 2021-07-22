from django.urls import path
from .views import category_list, post_detail, post_list


urlpatterns = [
    path('categories', category_list, name='category_list'),
    path('<str:category_name>/', post_list, name='post_list'),
    path('<str:category_name>/<int:post_pk>/', post_detail, name='post_detail'),
]

