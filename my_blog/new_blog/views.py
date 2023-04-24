from django.shortcuts import render

def home_page(request):
    return render(request,"new_blog/index.html")

def posts(request):
    pass

def post_info(request):
    pass