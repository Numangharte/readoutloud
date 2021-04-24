from django.urls import path,include
from . import views
urlpatterns = [
    path('' , views.new,name='new'),
    path('home' , views.home,name='home'),
    path('english' , views.english,name='english'),
    path('new' , views.new,name='new'),
]