from django.shortcuts import render, get_object_or_404
from rac_blog.models import BlogPost  # Import the BlogPost model from rac_blog app

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

<<<<<<< HEAD
#SERVICES 

def payroll_management(request):
    return render(request, "payroll_management.html")
=======
def blog_post_view(request):
    # Get all published blog posts
    blogs = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    
    # For debugging
    print(f"Number of blogs found: {blogs.count()}")
    
    return render(request, 'blog-post.html', {'blogs': blogs})

def blog_detail_view(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id, is_published=True)
    return render(request, 'blog-read-more.html', {'blog': blog})
>>>>>>> d237d900ac2df7a7f36b9243237a1860e5353b76
