
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import contact_usform
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return render(request, 'mainapp/home.html')

def colleges(request):
    college_list = ['SVEW', 'VIT', 'BVRICE']
    return render(request, 'mainapp/colleges.html', {'colleges': college_list})

def students(request):
    student_data = [
        {'name': 'Anita', 'branch': 'CSE', 'age': 19},
        {'name': 'Raju', 'branch': 'IT', 'age': 17},
        {'name': 'Suresh', 'branch': 'ECE', 'age': 21},
    ]
    return render(request, 'mainapp/students.html', {'students': student_data})

def address(request):
    return render(request, 'mainapp/address.html')

def contact_us(request):
    form = contact_usform(request.POST or None)
    if form.is_valid():
        send_mail(
            form.cleaned_data['subject'],
            form.cleaned_data['message'],
            settings.EMAIL_HOST_USER,
            [form.cleaned_data['to_email']]
        )
        return render(request, 'mainapp/contact_us.html', {'form': form, 'success': True})
    return render(request, 'mainapp/contact_us.html', {'form': form})
