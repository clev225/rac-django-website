from django.urls import path
from . import views

urlpatterns = [
    # Existing URLs
    path('login/', views.rac_blog_login, name='rac_blog_login'),
    
    # Blog form URLs
    path('blog-form/', views.blog_form, name='blog_form'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('blog-list/', views.blog_list, name='blog_list'),
]