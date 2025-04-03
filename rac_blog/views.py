from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import BlogPost, Announcement, Service
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from typing import Any



# Then in your functions, you can add type hints
def is_superadmin(user: User) -> bool:
    return user.is_superuser

# Update the user_passes_test decorator to redirect to custom login
def superadmin_required(function):
    actual_decorator = user_passes_test(
        is_superadmin,
        login_url='rac_blog_login'  # Redirect to custom login
    )
    return actual_decorator(function)

def rac_blog_login(request):
    # Check if user is already logged in
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('blog_list')
        
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
                messages.add_message(request, messages.SUCCESS, "Successfully logged in as RAC Admin", extra_tags='login_success')
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
    # Check if user is already logged in
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('blog_list')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # In specific places where you get warnings
        user = authenticate(request, username=username, password=password)  # type: ignore
        if user is not None and user.is_superuser:  # type: ignore
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Successfully logged in as RAC Admin", extra_tags='login_success')
            return redirect('blog_list')  # Changed from blog_form to blog_list
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
            
    return render(request, 'login.html')

@login_required(login_url='rac_blog_login')
@superadmin_required
def blog_form(request):
    return render(request, 'blog-form.html')

@login_required(login_url='rac_blog_login')
@superadmin_required
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
    
@login_required(login_url='rac_blog_login')
@superadmin_required
def edit_blog(request, blog_id):
    """
    View to display the blog edit form with pre-filled data
    """
    try:
        blog = BlogPost.objects.get(id=blog_id)
        return render(request, 'blog-form.html', {'blog': blog})
    except BlogPost.DoesNotExist:
        messages.error(request, "Blog not found.")
        return redirect('blog_list')

@login_required(login_url='rac_blog_login')
@superadmin_required
def update_blog(request, blog_id):
    """
    View to handle the blog update form submission
    """
    try:
        blog = BlogPost.objects.get(id=blog_id)
        
        if request.method == 'POST':
            # Get form data
            title = request.POST.get('title')
            author = request.POST.get('author')
            date_published = request.POST.get('date_published')
            description = request.POST.get('description')
            content = request.POST.get('content')
            
            # Update blog fields
            blog.title = title
            blog.author = author
            blog.date_published = date_published
            blog.description = description
            blog.content = content
            
            # Handle image upload
            if 'image' in request.FILES:
                # If a new image is uploaded, replace the old one
                blog.image = request.FILES['image']
            elif 'keep_image' not in request.POST:
                # If the checkbox is unchecked and no new image, remove the current image
                blog.image = None
            
            # Save the updated blog
            blog.save()
            
            messages.success(request, "Blog updated successfully!")
            return redirect('blog_detail', blog_id=blog.id)
        
        return render(request, 'blog-form.html', {'blog': blog})
    
    except BlogPost.DoesNotExist:
        messages.error(request, "Blog not found.")
        return redirect('blog_list')


@login_required(login_url='rac_blog_login')
@superadmin_required
def blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')  # Changed from Blog to BlogPost
    return render(request, 'blog-list.html', {'blogs': blogs})


@login_required(login_url='rac_blog_login')
@superadmin_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    blog.delete()
    messages.success(request, f'Blog "{blog.title}" has been deleted successfully.')
    return redirect('blog_list')


@login_required(login_url='rac_blog_login')
@superadmin_required
def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blog-detail.html', {'blog': blog})

# Add these views to your existing views.py file
@login_required(login_url='rac_blog_login')
@superadmin_required
def announcement_form(request):
    return render(request, 'announcement-form.html')

@login_required(login_url='rac_blog_login')
@superadmin_required
def create_announcement(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        date_published = request.POST.get('date_published')
        description = request.POST.get('description')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        # Create new announcement
        announcement = Announcement(
            title=title,
            author=author,
            date_published=date_published,
            description=description,
            content=content,
            image=image
        )
        announcement.save()
        
        messages.success(request, 'Announcement created successfully!')
        return redirect('announcement_list')
    
    return redirect('announcement_form')

@login_required(login_url='rac_blog_login')
@superadmin_required
def edit_announcement(request, announcement_id):
    """
    View to display the announcement edit form with pre-filled data
    """
    try:
        announcement = Announcement.objects.get(id=announcement_id)
        return render(request, 'announcement-form.html', {'announcement': announcement})
    except Announcement.DoesNotExist:
        messages.error(request, "Announcement not found.")
        return redirect('announcement_list')

@login_required(login_url='rac_blog_login')
@superadmin_required
def update_announcement(request, announcement_id):
    """
    View to handle the announcement update form submission
    """
    try:
        announcement = Announcement.objects.get(id=announcement_id)
        
        if request.method == 'POST':
            # Get form data
            title = request.POST.get('title')
            author = request.POST.get('author')
            date_published = request.POST.get('date_published')
            description = request.POST.get('description')
            content = request.POST.get('content')
            
            # Update announcement fields
            announcement.title = title
            announcement.author = author
            announcement.date_published = date_published
            announcement.description = description
            announcement.content = content
            
            # Handle image upload
            if 'image' in request.FILES:
                # If a new image is uploaded, replace the old one
                announcement.image = request.FILES['image']
            elif 'keep_image' not in request.POST:
                # If the checkbox is unchecked and no new image, remove the current image
                announcement.image = None
            
            # Save the updated announcement
            announcement.save()
            
            messages.success(request, "Announcement updated successfully!")
            return redirect('announcement_detail', announcement_id=announcement.id)
        
        return render(request, 'announcement-form.html', {'announcement': announcement})
    
    except Announcement.DoesNotExist:
        messages.error(request, "Announcement not found.")
        return redirect('announcement_list')

@login_required(login_url='rac_blog_login')
@superadmin_required
def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'announcements.html', {'blogs': announcements})

@login_required(login_url='rac_blog_login')
@superadmin_required
def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    announcement.delete()
    messages.success(request, f'Announcement "{announcement.title}" has been deleted successfully.')
    return redirect('announcement_list')

@login_required(login_url='rac_blog_login')
@superadmin_required
def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    return render(request, 'announcement-detail.html', {'announcement': announcement})

# Public view for announcements (no login required)
def public_announcements(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'public-announcements.html', {'blogs': announcements})

def add_services(request):
    services = Service.objects.all().order_by('-created_at')
    return render(request, 'add-services.html', {'services': services})

@login_required(login_url='rac_blog_login')
@superadmin_required
def service_form(request):
    return render(request, 'service-form.html')

@login_required(login_url='rac_blog_login')
@superadmin_required
def create_service(request):
    if request.method == 'POST':
        # Process the form data
        title = request.POST.get('title')
        
        # Set default values for removed fields
        author = "Admin"  # Default author value
        date_published = "2025-01-01"  # Default date
        
        # Create new service
        service = Service.objects.create(
            title=title,
            author=author,
            date_published=date_published,
            # No image field since it was removed
        )
        
        # Get descriptions
        description_count = int(request.POST.get('description_count', 0))
        descriptions = []
        for i in range(description_count):
            desc = request.POST.get(f'description_{i}')
            if desc:
                descriptions.append(desc)
        
        # Get requirements
        requirements = []
        category_count = int(request.POST.get('category_count', 0))
        for i in range(category_count):
            category = request.POST.get(f'category_{i}')
            if category:
                subcategories = []
                subcategory_count = int(request.POST.get(f'subcategory_count_{i}', 0))
                for j in range(subcategory_count):
                    subcat = request.POST.get(f'subcategory_{i}_{j}')
                    if subcat:
                        subcategories.append(subcat)
                
                requirements.append({
                    'category': category,
                    'subcategories': subcategories
                })
        
        # Process contact information
        contacts = []
        contact_count = int(request.POST.get('contact_count', 0))
        for i in range(contact_count):
            name = request.POST.get(f'contact_name_{i}')
            phone = request.POST.get(f'contact_phone_{i}')
            email = request.POST.get(f'contact_email_{i}')
            image = request.POST.get(f'contact_image_{i}')
            
            if name:
                contacts.append({
                    'name': name,
                    'phone': phone or '',
                    'email': email or '',
                    'image': image or ''
                })
        
        # Save the service with JSON fields
        service.descriptions = descriptions
        service.requirements = requirements
        service.contacts = contacts
        service.save()
        
        # Get the redirect URL from the form or default to add_services
        redirect_url = request.POST.get('redirect_url', 'add_services')
        
        # Add a success message
        messages.success(request, f'Service "{title}" has been created successfully!')
        
        # Redirect to the specified URL
        return redirect(redirect_url)
    
    # If not POST, redirect to service form
    return redirect('service_form')

@login_required(login_url='rac_blog_login')
@superadmin_required
def update_service(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
        
        if request.method == 'POST':
            # Get form data
            title = request.POST.get('title')
            
            # Keep existing values for removed fields
            author = service.author
            date_published = service.date_published
            
            # Process descriptions
            descriptions = []
            description_count = int(request.POST.get('description_count', 0))
            for i in range(description_count):
                desc = request.POST.get(f'description_{i}')
                if desc:
                    descriptions.append(desc)
            
            # Process requirements
            requirements = []
            category_count = int(request.POST.get('category_count', 0))
            for i in range(category_count):
                category = request.POST.get(f'category_{i}')
                if category:
                    subcategories = []
                    subcategory_count = int(request.POST.get(f'subcategory_count_{i}', 0))
                    for j in range(subcategory_count):
                        subcat = request.POST.get(f'subcategory_{i}_{j}')
                        if subcat:
                            subcategories.append(subcat)
                            
                            requirements.append({
                                'category': category,
                                'subcategories': subcategories
                            })
                            
                            # Update service fields
                            service.title = title
                            service.descriptions = descriptions
                            service.requirements = requirements
                            
                            # Handle image upload
                            if 'image' in request.FILES:
                                # If a new image is uploaded, replace the old one
                                service.image = request.FILES['image']
                            elif 'keep_image' not in request.POST:
                                # If the checkbox is unchecked and no new image, remove the current image
                                service.image = None
                            
                            # Save the updated service
                            service.save()
                            
                            messages.success(request, "Service updated successfully!")
                            return redirect('service_detail', service_id=service.id)
                            
                            return render(request, 'service-form.html', {'service': service})
                        
    except Service.DoesNotExist:
        messages.error(request, "Service not found.")
        return redirect('add_services')

@login_required(login_url='rac_blog_login')
@superadmin_required
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    messages.success(request, f'Service "{service.title}" has been deleted successfully.')
    return redirect('add_services')

@login_required(login_url='rac_blog_login')
@superadmin_required
def service_detail(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
        return render(request, 'service-detail.html', {'service': service})
    except Service.DoesNotExist:
        # Make sure there's proper indentation and no syntax errors here
        messages.error(request, "Service not found.")
        return redirect('add_services')

