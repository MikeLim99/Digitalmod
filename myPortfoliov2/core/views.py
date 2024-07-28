from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import *

from .models import Post
# Create your views here.

def home(request):
    keyService = Services.objects.all()
    return render(request, 'home.html', {'keyService':keyService})

class blogs(ListView):
    model = Post
    template_name = 'blogs.html'
    ordering = ['-id']

class detailedBlog(DetailView):
    model = Post
    template_name = 'detailed_blog.html'

def contacts(request):
    if request.method == "POST":
        Name = request.POST['Name']
        cx_email = request.POST['email']
        subject = request.POST['subject']
        feedback = request.POST['feedback']

        send_mail(
            'Name: ' + Name + ', Subject: ' + subject + ', ' + cx_email, # subject
            feedback, # message
            cx_email, # sender's email email
            ['agshards@gmail.com'] # receiver's email
        )
        messages.success(request, ('Your message has been sent! Thank you for your response.'))
        return render(request, 'contacts.html', {})
    else:
        return render(request, 'contacts.html', {})

def portfolio(request):
    galleries = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'galleries':galleries})

def detailedPortfolio(request, id):
    galleries = Portfolio.objects.all()
    gallery = get_object_or_404(Portfolio, id=id)
    image = PortfolioGallery.objects.filter(portfolio=gallery)
    return render(request, 'detailed_portfolio.html', {'gallery': gallery, 'image':image, 'galleries':galleries })