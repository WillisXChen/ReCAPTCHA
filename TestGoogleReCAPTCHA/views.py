from datetime import datetime
from django.shortcuts import render


def hello_world1(request):
    return render(request, 'hello_google_reCAPTCHA1.html', {
        'current_time': str(datetime.now()),
    })
    
def hello_world2(request):
    return render(request, 'hello_google_reCAPTCHA2.html', {
        'current_time': str(datetime.now()),
    })
    
def hello_world3(request):
    return render(request, 'hello_google_reCAPTCHA3.html', {
        'current_time': str(datetime.now()),
    })
    
def hello_world4(request):
    return render(request, 'hello_google_reCAPTCHA4.html', {
        'current_time': str(datetime.now()),
    })