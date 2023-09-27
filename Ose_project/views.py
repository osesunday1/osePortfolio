from django.shortcuts import render
from django.shortcuts import redirect
from clientfeedback.forms import *
from clientfeedback.models import *


def home (request):

    form = ClientFeedbackForm()
    if request.method == 'POST': 
        form = ClientFeedbackForm(request.POST)
        if form.is_valid(): 
            form.save(commit=True) 
            return redirect('home') 
        else:
             print(form.errors)

    context = {'form': form}

    return render (request, 'home.html', context)








def downloadfile(request):
    
    downloadfile = "https://www.dropbox.com/scl/fi/bnr0o22i4eymdhie9zn0e/Resume-Oseyenbhin.pdf?rlkey=eb5krwvmi89cfvs4spe84polz&dl=0"
    
    
    return redirect(downloadfile)