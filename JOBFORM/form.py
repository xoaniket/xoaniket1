

from django import forms
from .models import JobApplication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class JobApplicationForm(forms.ModelForm):
     pincode = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'6-digit pincode'
        })),
     class Meta:
        model = JobApplication
        exclude = ['job']   # hidden on form

        

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'skills': forms.Textarea(attrs={'rows': 2, 'class':'form-control'}),
            'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'10-digit mobile number'}),
            'profile_photo': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control', 'rows': 3}),
            'city': forms.TextInput(attrs={'class':'form-control'}),

            'higest_qualification': forms.TextInput(attrs={'class':'form-control'}),
            'university_name': forms.TextInput(attrs={'class':'form-control'}),
            'passing_year': forms.NumberInput(attrs={'class':'form-control', 'min':1900, 'max':2100}),
            'experience': forms.NumberInput(attrs={'class':'form-control', 'min':0, 'step':1}),
            'last_company': forms.TextInput(attrs={'class':'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }
        



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    username = forms.CharField(
        label="USERNAME",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password1 = forms.CharField(
        label="PASSWORD",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
    password2 = forms.CharField(
        label="CONFIRM PASSWORD",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
    )

   



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="USERNAME",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        label="PASSWORD",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
   







