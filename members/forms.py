from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class sign_up_form(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    location=(forms.CharField(max_length=20))

    class Meta:
        model=User
        fields = ('username','first_name','last_name','email','location','password1','password2')

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.TextInput(attrs={'class':'form-control'}),
            'password2': forms.TextInput(attrs={'class':'form-control'}),      
        }