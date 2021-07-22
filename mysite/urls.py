from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include("rest_framework.urls")),
    path('rest-auth/', include("rest_auth.urls")),
]
