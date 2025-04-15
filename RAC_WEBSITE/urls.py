from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import the error handler views
from .views import handler404, handler500, handler403, handler400

urlpatterns = [
    # Your existing URL patterns
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Register error handlers
handler404 = 'RAC_WEBSITE.views.handler404'
handler500 = 'RAC_WEBSITE.views.handler500'
handler403 = 'RAC_WEBSITE.views.handler403'
handler400 = 'RAC_WEBSITE.views.handler400'