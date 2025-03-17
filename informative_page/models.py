from django.db import models

# Create your models here.
def index_view(request):
    return render(request, 'informative_page/index.html')

def about_us_view(request):
    return render(request, 'informative_page/about-us.html')