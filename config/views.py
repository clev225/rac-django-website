from django.shortcuts import render

def handler404(request, exception):
    context = {
        'error_code': '404',
        'error_title': 'Page Not Found',
        'error_message': 'The page you are looking for does not exist.'
    }
    return render(request, 'error_page.html', context, status=404)

def handler500(request):
    context = {
        'error_code': '500',
        'error_title': 'Server Error',
        'error_message': 'Something went wrong on our end. Please try again later.'
    }
    return render(request, 'error_page.html', context, status=500)

def handler403(request, exception):
    context = {
        'error_code': '403',
        'error_title': 'Forbidden',
        'error_message': 'You do not have permission to access this page.'
    }
    return render(request, 'error_page.html', context, status=403)

def handler400(request, exception):
    context = {
        'error_code': '400',
        'error_title': 'Bad Request',
        'error_message': 'The request could not be understood by the server.'
    }
    return render(request, 'error_page.html', context, status=400)