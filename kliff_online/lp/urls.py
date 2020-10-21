from django.urls import path

from . import views

urlpatterns = [
    path('', views.landingPage),
    path('pt/', views.landingPage),
    path('obrigado/', views.thankYou),
    path('en/', views.landingPageEN),
    path('thanks/', views.thankYouEN),
]
