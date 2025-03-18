from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test

def is_superadmin(user):
    return user.is_superuser

def rac_blog_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('blog_form')  # Redirect to blog form if login is successful
        else:
            return render(request, 'rac_blog/login.html', {'error': 'Invalid credentials or not a superadmin'})

    return render(request, 'rac_blog/login.html')

def custom_login(request):
    return render(request, 'login.html')

@login_required
@user_passes_test(is_superadmin)
def blog_form(request):
    return render(request, 'rac_blog/blog-form.html')
