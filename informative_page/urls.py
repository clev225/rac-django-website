from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Homepage
    path("about-us/", views.about_us, name="about_us"),
    path("services/", views.services, name="services"),
    #services get started button
    path('payroll-management/', views.payroll_management, name='payroll_management'),
    path('business-registration/', views.business_registration, name='business_registration'),
    path('auditing_services/', views.auditing_services, name='auditing_services'),
    path('tax_compliance/', views.tax_compliance, name='tax_compliance'),
    path('business_formation_registration/', views.business_formation_registration, name='business_formation_registration'),
    path('contact_review_preparation/', views.contract_review_preparation, name='contract_review_preparation'),
    path('corporate_governance_compliance/', views.corporate_governance_compliance, name='corporate_governance_compliance'),
    path('employment_labor_law_support/', views.employment_labor_law_support, name='employment_labor_law_support'),
    path('mergers_acquisition_restructuring/', views.mergers_acquisition_restructuring, name='mergers_acquisition_restructuring'),
    path('ip_assistance/', views.ip_assistance, name='ip_assistance'),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("team/", views.team, name="team"),
    path('blog/<int:blog_id>/', views.blog_detail_view, name='blog_detail'),
    # Add this URL pattern to the urlpatterns list
    path('announcements/', views.info_announcements, name='info_announcements'),
    # Add this URL pattern to the urlpatterns list
    path('announcements/<int:announcement_id>/', views.announcement_read_more, name='announcement_read_more'),
    # Add these URL patterns to the urlpatterns list
    path('blogs/', views.blog_post, name='blog_post'),
    path('blogs/<int:blog_id>/', views.blog_read_more, name='blog_read_more'),
]