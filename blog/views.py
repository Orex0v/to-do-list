from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
import datetime
from .models import Post
from .forms import PostForm, CompliteForm, SignUpForm



def post_list(request):
    posts = Post.objects.filter(compile_post=False).order_by('-deadline')
    return render(request, 'blog/post_list.html', {'posts' : posts, 'now': timezone.now})


def post_complite(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.compile_post = not post.compile_post
    post.save()
    return  redirect( '/')


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        phone_number = form.cleaned_data.get('phone_number')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


def complite_post_list(request):
    posts = Post.objects.filter(compile_post=True).order_by('-deadline')
    return render(request, 'blog/complite.html', {'posts' : posts, 'now': timezone.now})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            # post.deadline = request.deadline
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            # post.complite = form.complite
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post' : post})
