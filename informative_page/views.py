from django.shortcuts import render, get_object_or_404
from rac_blog.models import BlogPost  # Import the BlogPost model from rac_blog app
from rac_blog.models import Announcement

def index(request):
    return render(request, "index.html")

def about_us(request):
    return render(request, "about-us.html")

def services(request):
    return render(request, "services.html")

def testimonials(request):
    return render(request, "testimonials.html")

def team(request):
    return render(request, "team.html")

def blogs(request):
    return render(request, "blog-post.html")

#SERVICES 

<<<<<<< HEAD
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
=======
def payroll_management(request):
    return render(request, "payroll_management.html")
>>>>>>> 7bf3dad088d394a6ffd278c23687dd90b3d64688
