from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.blog_home, name='blog_home'),
    path('category/<str:cat>',views.blog_home, name='blog_home'),
    path('details/<int:pid>', views.blog_details, name='blog_details')
]