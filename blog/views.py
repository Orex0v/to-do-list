from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import datetime
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(compile_post=False).order_by('-deadline')
    # if request.method == "POST":
    #     form = CompliteForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.compile_post = True
    #         post.published_date = timezone.now()
    #         post.save()
    #         return redirect('post_detail', pk=post.pk)
    #     else:
    #         form = CompliteForm()
    return render(request, 'blog/post_list.html', {'posts' : posts, 'now': timezone.now})

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
    return render(request, 'blog/post_edit.html', {'form': form})

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        return render(request, 'blog/signup.html', {'form': form})
  else:
    form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

# def post_complete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.complete_data = timezone.now()
#             post.complite = True
#             post.save()
#             return redirect('/', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, '/', {'form': form})
