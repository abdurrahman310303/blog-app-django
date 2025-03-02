from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib import messages


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog-home")
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("blog-home")

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog-home")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('blog-home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return redirect('blog-home')  # Prevent unauthorized access

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'update_post.html', {'form': form})