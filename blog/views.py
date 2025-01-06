from django.shortcuts import render , redirect
from .models import Post
from .forms import *

# Create your views here.
def new_post(request):

    if request.method == 'POST' :
        # form = newpostform(request.POST)
        if newpostform(request.POST).is_valid() :
            newpostform(request.POST).save()
            return redirect('blog:post_show')
    else :
        form = newpostform()
        return render(request , 'blog/post_new.html' , {'form' : form})


def detail(request , id):
    posts = Post.objects.get(id=id)
    return render(request , 'blog/detail.html', {'posts' : posts})
def post_show(request):
    posts = Post.objects.filter(status='pub')
    return render(request, 'blog/home.html', {'posts' : posts })

def update_post(request , id):
    post = Post.objects.get(id=id)
    form = newpostform(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return  redirect('blog:post_show')
    return render(request , 'blog/post_new.html' , {'form' : form})
def delete_post(request , id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_show')
    return render(request , 'blog/delete.html' , {'post' : post})