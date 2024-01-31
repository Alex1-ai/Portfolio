from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Personal_Information, Experience, Achievement, Education,Skills,Portfolio,Contact
from blog.models import Blog
import os
from django.http import JsonResponse


# from django.shortcut import render
# Create your views here.

def download_cv(request):
    # Assuming there's only one Personal_Information instance
    personal_info = Personal_Information.objects.first()

    # Check if the CV file exists
    if personal_info and personal_info.cv and os.path.exists(personal_info.cv.path):
        with open(personal_info.cv.path, 'rb') as cv_file:
            # Set response headers
            response = HttpResponse(cv_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{personal_info.first_name}_{personal_info.last_name}_CV.pdf"'
            return response
    else:
        # Handle the case where the CV file or Personal_Information instance does not exist
        return render(request, 'index.html')  


def home(request):
    return render(request,'index.html')


def about(request):
    personal_info = Personal_Information.objects.first()
    achievement = Achievement.objects.first()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skills.objects.all()
    # print("skills ",skills[0].name)
    context = {
        "personal_info": personal_info,
        "achievement": achievement,
        "educations": educations,
        "experiences": experiences,
        "skills": skills

    }
    return render(request, 'about.html', {"context":context})

def portfolio(request):
    portfolios = Portfolio.objects.all()

    context = {
        "portfolios" : portfolios
    }
    
    # print(portfolios[0].langauge)
    return render(request, 'portfolio.html' , {"context": context})

def contact(request):
    if request.method == 'POST':
        # print("Entered here")
        
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            # print(name, email, subject, message)
            message = f"Name: {name} \n emial : {email} \n subject: {subject} \n message: {message}"
            contact_us = Contact.objects.create(
                name=name, email=email,  subject=subject, message=message)
            # return redirect('contact')
        except:
            messages.warning(
                request, "Please Try Again, Something Went Wrong. Hint: please kindly check your internet connection")
            return redirect('contact')

        adminEmail = 'alexanderemmanuel1719@gmail.com'
        subject = 'ALEXIS PORTFOLIO'
        email_message = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [adminEmail],
        )
        try:
            email_message.send()
            contact_us.save()
            # messages.info(
            #     request, f'Message sent successfully . Thanks {name} for the contacting us we get to you as soon as possible')
            # return redirect('home')
            response_data = {'result': 'success'}
            return JsonResponse(response_data)
        except:
            response_data = {'result': 'error'}
            return JsonResponse(response_data)
            # messages.warning(
            #     request, "Please Try Again, Something Went Wrong. Hint: please kindly check your internet connection")
            # return redirect('contact')

        # message = request.POST['message']

    else:
       # print("It is not post")
        return render(request, 'contact.html')

def blog(request):
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs
    }
    return render(request, 'blog.html', {"context": context})


def blogDetails(request, pk):
    # print(pk)
    single_blog = get_object_or_404(Blog, pk=pk)
    paragraphs = single_blog.content.split('\n')
    return render(request, 'blog-post.html', {'single_blog': single_blog, 'paragraphs': paragraphs})
    
