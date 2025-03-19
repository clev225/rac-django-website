from django.urls import path
from .views import rac_blog_login, blog_form

urlpatterns = [
    path('admin/', rac_blog_login, name='rac_blog_login'),
    path('blog-form/', blog_form, name='blog_form'),  # ✅ Correct existing URL
    path('blog_form/', blog_form, name='blog_form_alt'),  # ✅ Optional alternative
]