from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import BlogPost
from django.shortcuts import get_object_or_404, redirect

def is_superadmin(user):
    return user.is_superuser

def rac_blog_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"DEBUG: Login Attempt - Username: {username}, Password: {password}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(f"DEBUG: Authentication successful for {user.username}")

            if user.is_superuser:
                login(request, user)
                print(f"DEBUG: Redirecting to blog_list")
                return redirect('blog_list')  # Changed from blog_form to blog_list
            else:
                print("DEBUG: User is not a superadmin!")
                return render(request, 'login.html', {'error': 'You must be a superadmin to log in.'})
        else:
            print("DEBUG: Authentication failed!")
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    print("DEBUG: Rendering login page")
    return render(request, 'login.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('blog_list')  # Changed from blog_form to blog_list
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials or not a superadmin'})
            
    return render(request, 'login.html')

@login_required
@user_passes_test(is_superadmin)
def blog_form(request):
    return render(request, 'blog-form.html')

@login_required
@user_passes_test(is_superadmin)
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        date_published = request.POST.get('date_published')
        description = request.POST.get('description')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        # Create new blog post
        blog = BlogPost(  # Changed from Blog to BlogPost
            title=title,
            author=author,
            date_published=date_published,
            description=description,
            content=content,
            image=image
        )
        blog.save()
        
        messages.success(request, 'Blog post created successfully!')
        return redirect('blog_list')
    
    return redirect('blog_form')


@login_required
@user_passes_test(is_superadmin)
def blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')  # Changed from Blog to BlogPost
    return render(request, 'blog-list.html', {'blogs': blogs})


@login_required
@user_passes_test(is_superadmin)
def delete_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    blog.delete()
    messages.success(request, f'Blog "{blog.title}" has been deleted successfully.')
    return redirect('blog_list')


@login_required
@user_passes_test(is_superadmin)
def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blog-detail.html', {'blog': blog})

