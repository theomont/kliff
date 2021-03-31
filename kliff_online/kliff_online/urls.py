"""kliff_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # < sitemap and robots.txt serve via TemplateView
#from django.contrib.sitemaps.views import sitemap # < sitemap

urlpatterns = [
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="application/xml")),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('admin/', admin.site.urls),
    path('', include('lp.urls')),
    path('tercio/', include('TMarq.urls')),
    path('home/', include('website.urls')),
    
]
