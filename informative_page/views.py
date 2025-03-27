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

def blog_post_view(request):
    # Get all published blog posts
    blogs = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    
    # For debugging
    print(f"Number of blogs found: {blogs.count()}")
    
    return render(request, 'blog-post.html', {'blogs': blogs})

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