from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),

    
]