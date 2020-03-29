from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bib-home'),
    path('about/', views.about, name='bib-about'),
]