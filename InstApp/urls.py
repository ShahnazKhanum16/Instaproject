from django.urls import path 
from .import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('Search/', views.search, name ='search'),
    path('Explore/', views.explore, name ='explore'),
    path('Reels/', views.reels, name ='reels'),
    path('Messages/', views.messages, name ='messages'),
    path('Notification/', views.notification, name ='notification'),
    path('Create/', views.create, name ='create'),
    path('Profile/', views.profile, name ='profile'),
    path('More/', views.more, name ='more'),
    
]
