from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Post

#Represents the main webpage and includes links to all other web pages
def index(request):
  return render(request, 'index.html')

#base.html: Includes the common elements shared by all web pages,
#such as the header and footer
def base(request):
  return render(request, 'base.html')


#users.html: Displays a list of all users, including their usernames and emails.
def users(request, users_id):
  #myusers = User.objects.get( pk=users_id )
  myusers = users.objects.all()

  return render(request, 'users.html',{'myusers': myusers})

def blogs(request):
  return render(request, 'blogs.html')

def comments(request):
  return render(request, 'comments.html', {})

def categories(request):
  return render(request, 'categories.html', {})


def blogdetails(request):
  return render(request, 'blogdetails.html')


