from django.urls import path, include
from . import views

urlpatterns = [
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
]
