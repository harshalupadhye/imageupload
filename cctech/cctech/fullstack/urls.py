from django.contrib import admin
from django.urls import path
from fullstack import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('submit/',views.submitUser, name="submit"),
    

    
]
