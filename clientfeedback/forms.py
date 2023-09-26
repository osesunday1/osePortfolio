from django import forms
from django.forms import ModelForm
from .models import *

#CREATE Feedback Form

class ClientFeedbackForm(ModelForm):
    email= forms.EmailInput()
    name = forms.TextInput()
    message = forms.TextInput()
    class Meta: 
        model = ClientFeedback
        fields= ('email','name', 'message')

        widgets= {
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': "Your Email"}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Full Name"}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder': "Talk to me b'cos i'm your guy"}),
        }

        labels= {
            'name': '',
            'email': '',
            'message': '',
        }

         
    