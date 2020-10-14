from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import LeadForm
from .models import Lead

def landingPage(request): 
    if request.method == 'POST': # Need to deal with subimited empty form (there is a HTML treatment, but have to deal in backend too)
        form = LeadForm(request.POST)
        if form.is_valid() : # Need an error treatment
            lead = form.save(commit=False)
            lead.save()
            return redirect('../obrigado/')
    else:
        return render(request, 'lp/landingpage.html')

def thankYou(request):
    return render(request, 'lp/thankyou.html')



