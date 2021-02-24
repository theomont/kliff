from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage),
    #path('pt/', views.homePage),
    #path('en/', views.homePageEN),
]
