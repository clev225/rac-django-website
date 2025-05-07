from django.shortcuts import render, get_object_or_404
from rac_blog.models import BlogPost  # Import the BlogPost model from rac_blog app
from rac_blog.models import Announcement

def index(request):
    return render(request, "index.html")

def about_us(request):
    return render(request, "about-us.html")

def services(request):
    return render(request, "services.html")

def faqs(request):
    return render(request, "faqs.html")

#services get started button
def payroll_management(request):
    return render(request, 'payroll_management.html')

def business_registration(request):
    return render(request, 'business_registration.html')

def auditing_services(request):
    return render(request, 'auditing_services.html')

def tax_compliance(request):
    return render(request, 'tax_compliance.html')

def business_formation_registration(request):
    return render(request, 'business_formation_registration.html')

def contract_review_preparation(request):
    return render(request, 'contract_review_preparation.html')

def corporate_governance_compliance(request):
    return render(request, 'corporate_governance_compliance.html')

def employment_labor_law_support(request):
    return render(request, 'employment_labor_law_support.html')

def mergers_acquisition_restructuring(request):
    return render(request, 'mergers_acquisition_restructuring.html')

def ip_assistance(request):
    return render(request, 'ip_assistance.html'
    )
def testimonials(request):
    return render(request, "testimonials.html")

def team(request):
    return render(request, "team.html")

def blogs(request):
    return render(request, "blog-post.html")


def info_announcements(request):
    announcements = Announcement.objects.all().order_by('-date_published')
    return render(request, 'info-announcements.html', {'announcements': announcements})

# Add this view function for the announcement detail page
def announcement_read_more(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    return render(request, 'announcement-read-more.html', {'announcement': announcement})

# Add these view functions
def blog_post(request):
    blogs = BlogPost.objects.all().order_by('-date_published')
    return render(request, 'blog-post.html', {'blogs': blogs})

def blog_read_more(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blog-read-more.html', {'blog': blog})

# Add this view function to handle the blog_detail URL
def blog_detail_view(request, blog_id):
    # This function should redirect to the blog_read_more view
    # or you can implement the detail view logic here
    return blog_read_more(request, blog_id)


# ERROR HANDLING PAGES
def handler404(request, exception):
    context = {
        'error_code': '404',
        'error_title': 'Page Not Found',
        'error_message': 'The page you are looking for does not exist.'
    }
    return render(request, 'error_page.html', context, status=404)


def handler403(request, exception):
    context = {
        'error_code': '403',
        'error_title': 'Forbidden',
        'error_message': 'You do not have permission to access this page.'
    }
    return render(request, 'error_page.html', context, status=403)

def handler400(request, exception):
    context = {
        'error_code': '400',
        'error_title': 'Bad Request',
        'error_message': 'The request could not be understood by the server.'
    }
    return render(request, 'error_page.html', context, status=400)