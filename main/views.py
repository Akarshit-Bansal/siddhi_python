from django.shortcuts import render
from .models import JobSeeker

def home(request):
    return render(request, 'About.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        cv = request.FILES.get('cv')

        JobSeeker.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
            cv=cv
        )

        return render(request, 'contact.html', {
            'success': True
        })

    return render(request, 'contact.html')