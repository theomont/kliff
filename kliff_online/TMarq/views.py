from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

#from .forms import LeadForm
#from .models import Lead

def landingPage(request): 
    return render(request, 'TMarq/landingpage.html')




