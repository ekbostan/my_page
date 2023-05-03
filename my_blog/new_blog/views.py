from django.shortcuts import render,get_object_or_404
from .models import Post

def home_page(request):
    prioritized_projects = Post.objects.all().order_by("-importance")[:3]
    return render(request,"new_blog/index.html",{
        "posts":prioritized_projects
    })

def about_me_page(request):
    return render(request,"new_blog/about.html")

def posts(request):
    all_posts = Post.objects.all()
    return render(request,"new_blog/posts.html", {"posts":all_posts})

def post_info(request,slug):
        
    identified_project = get_object_or_404(Post,slug=slug)
    return render(request,"new_blog/posts.html",{"post":identified_project})