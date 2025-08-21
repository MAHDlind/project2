from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_us, name='contact_page'),
    path('get_start/', views.get_start, name='get_start_page'),
    path('newslatter/', views.newsletter, name='newsletter'),
]