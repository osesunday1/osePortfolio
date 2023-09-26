from django.shortcuts import render
from django.http import StreamingHttpResponse
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
    # Dropbox URL of the file you want to link
    downloadfile = "https://www.dropbox.com/scl/fi/3mgge4gxixjdm5sq3g3vt/Resume-Oseyenbhin.pdf?rlkey=fskdi591bcobn77jo4n3wfwyn&dl=0"
    
    return redirect(downloadfile)