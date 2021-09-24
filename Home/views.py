from django.shortcuts import render, redirect
from .models import Posts


# Create your views here.
def home(request):
    posts = Posts.objects.all()
    ctx = {'posts': posts}
    return render(request, 'Home.html', ctx)


