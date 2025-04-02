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

    # Service URLs
    path('add-services/', views.add_services, name='add_services'),
    path('service-form/', views.service_form, name='service_form'),
    path('create-service/', views.create_service, name='create_service'),
    path('edit-service/<int:service_id>/', views.edit_service, name='edit_service'),
    path('update-service/<int:service_id>/', views.update_service, name='update_service'),
    path('delete-service/<int:service_id>/', views.delete_service, name='delete_service'),
    path('service-detail/<int:service_id>/', views.service_detail, name='service_detail'),
]
