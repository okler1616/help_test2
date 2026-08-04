from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post_detail.html", {"post": post})