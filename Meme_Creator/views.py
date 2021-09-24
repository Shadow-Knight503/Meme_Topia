from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PostForm
from cloudinary.forms import cl_init_js_callbacks


# Create your views here.
def memepost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('https://youtu.be/dQw4w9WgXcQ')
    form = PostForm()
    ctx = {'form': form}
    return render(request, 'Uploader.html', ctx)
