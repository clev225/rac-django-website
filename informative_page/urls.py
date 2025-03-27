from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Homepage
    path("about-us/", views.about_us, name="about_us"),
    path("services/", views.services, name="services"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("team/", views.team, name="team"),
<<<<<<< HEAD
    path('blog/<int:blog_id>/', views.blog_detail_view, name='blog_detail'),
    # Add this URL pattern to the urlpatterns list
    path('announcements/', views.info_announcements, name='info_announcements'),
    # Add this URL pattern to the urlpatterns list
    path('announcements/<int:announcement_id>/', views.announcement_read_more, name='announcement_read_more'),
    # Add these URL patterns to the urlpatterns list
    path('blogs/', views.blog_post, name='blog_post'),
    path('blogs/<int:blog_id>/', views.blog_read_more, name='blog_read_more'),
=======
    path("blogs/", views.blogs, name="blogs"),
    path("payroll_management/", views.payroll_management, name="payroll_management")
>>>>>>> 7bf3dad088d394a6ffd278c23687dd90b3d64688
]