from django.shortcuts import render

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

def payroll_management(request):
    return render(request, "payroll_management.html")