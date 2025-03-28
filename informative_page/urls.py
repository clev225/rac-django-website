from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Homepage
    path("about-us/", views.about_us, name="about_us"),
    path("services/", views.services, name="services"),
    #services get started button
    path('services/payroll-management/', views.payroll_management, name='payroll_management'),
    path('services/business-registration/', views.business_registration, name='business_registration'),
    path('services/auditing_services/', views.auditing_services, name='auditing_services'),
    path('services/tax_compliance/', views.tax_compliance, name='tax_compliance'),
    path('services/business_formation_registration/', views.business_formation_registration, name='business_formation_registration'),
    path('services/contact_review_preparation/', views.contract_review_preparation, name='contract_review_preparation'),
    path('services/corporate_governance_compliance/', views.corporate_governance_compliance, name='corporate_governance_compliance'),
    path('services/employment_labor_law_support/', views.employment_labor_law_support, name='employment_labor_law_support'),
    path('services/mergers_acquisition_restructuring/', views.mergers_acquisition_restructuring, name='mergers_acquisition_restructuring'),
    path('services/ip_assistance/', views.ip_assistance, name='ip_assistance'),
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