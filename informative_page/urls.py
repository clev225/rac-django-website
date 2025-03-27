from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Homepage
    path("about-us/", views.about_us, name="about_us"),
    path("services/", views.services, name="services"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("team/", views.team, name="team"),
    path("blogs/", views.blogs, name="blogs"),
<<<<<<< HEAD
    path("payroll_management/", views.payroll_management, name="payroll_management")
=======
    path('blog/', views.blog_post_view, name='blog_post'),
    path('blog/<int:blog_id>/', views.blog_detail_view, name='blog_detail'),
>>>>>>> d237d900ac2df7a7f36b9243237a1860e5353b76
]