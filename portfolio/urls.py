from django.urls import path
from . import views
# from django.contrib.auth import 

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name="portfolio"),
    path('contact', views.contact, name="contact"),
    path('blog', views.blog, name="blog"),
    path('blog-detail/<str:pk>', views.blogDetails, name="blog-detail"),

    path('download-cv/', views.download_cv, name='download_cv'),
]