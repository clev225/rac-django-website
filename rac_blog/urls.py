from django.urls import path
from django.contrib.auth.views import LogoutView  # Add this import
from . import views

urlpatterns = [
    # Existing URLs
    path('login/', views.rac_blog_login, name='rac_blog_login'),
    
    # Blog form URLs
    path('blog-form/', views.blog_form, name='blog_form'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('blog-list/', views.blog_list, name='blog_list'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('update_blog/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    
    # Announcement URLs
    path('announcement_form/', views.announcement_form, name='announcement_form'),
    path('create_announcement/', views.create_announcement, name='create_announcement'),
    path('edit_announcement/<int:announcement_id>/', views.edit_announcement, name='edit_announcement'),
    path('update_announcement/<int:announcement_id>/', views.update_announcement, name='update_announcement'),
    path('announcement_list/', views.announcement_list, name='announcement_list'),
    path('delete_announcement/<int:announcement_id>/', views.delete_announcement, name='delete_announcement'),
    path('announcement_detail/<int:announcement_id>/', views.announcement_detail, name='announcement_detail'),
    path('announcements/', views.public_announcements, name='public_announcements'),

]
