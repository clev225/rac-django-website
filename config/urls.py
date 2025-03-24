"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.shortcuts import redirect
from rac_blog import views  # Import your blog app views
from django.conf import settings  # Add this import
from django.conf.urls.static import static

urlpatterns = [
    path("", include("informative_page.urls")),  # Make informative_page the default app
    path("", include("rac_blog.urls")),  # ✅ Ensure rac_blog URLs are loaded

    # Redirect ANY URL that ends with `/admin` to your custom login page
    re_path(r'^.*admin$', lambda request: redirect('/rac_blog/login/'), name='custom_admin_redirect'),

    # Custom login page
    path('rac_blog/login/', views.custom_login, name='custom_login'),

    # (Optional) Keep the original Django admin panel, but at a different URL
    path('secure-admin/', admin.site.urls),  

    path('rac_blog/', include('rac_blog.urls')),
]

# Add this to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)