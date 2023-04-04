from django.urls import path, include

from . import views

from . import tempURL

urlpatterns = [
    path('register/', views.register),
    path('register/register_success', views.register_success),
    path('account/', views.account),
    path('account/', include('django.contrib.auth.urls')),
    path('register/<str:signed_data>/', tempURL.temp, name='temp'),
]
