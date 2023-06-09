from django.urls import path 
from.import views

urlpatterns = [
    path("",views.home_page,name="home-page"),
    path("posts",views.posts,name="post-page"),
    path("about",views.about_me_page,name="about-me-page"),
    path("posts/<slug:slug>/",views.post_info,name="post-info-page"),
]