from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

#from .forms import LeadForm
#from .models import Lead

def homePage(request): 
    return render(request, 'home/homepage.html')
    
#    if request.method == 'POST': # Need to deal with subimited empty form (there is a HTML treatment, but have to deal in backend too)
#        form = LeadForm(request.POST)
#        if form.is_valid() : # Need an error treatment
#            lead = form.save(commit=False)
#            lead.save()
#            return redirect('../obrigado/')
#    else:
#        return render(request, 'home/homepage.html')

#def homePageEN(request): 
#    if request.method == 'POST': # Need to deal with subimited empty form (there is a HTML treatment, but have to deal in backend too)
#        form = LeadForm(request.POST)
#        if form.is_valid() : # Need an error treatment
#            lead = form.save(commit=False)
#            lead.save()
#            return redirect('../thanks/')
#    else:
#        return render(request, 'lp/landingpage-en.html')

#def homeYouEN(request):
#    return render(request, 'lp/thankyou-en.html')