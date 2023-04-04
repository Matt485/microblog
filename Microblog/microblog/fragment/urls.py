from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_page),
    path('about/', views.about_page),
    path('help/', views.help_page),
    path('privacy-policy/', views.privacy_policy),
    path('faq/', views.faq_page),
    path('blog/<str:blog_name>/', views.blog),
    path('blog/<str:blog_name>/archive', views.blog_archive),
    path('blog/<str:blog_name>/about', views.blog_about),
]
