
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import sign_up_form
# Create your views here.


class sign_up_view(generic.CreateView):
    form_class=sign_up_form
    template_name='registration/register.html'
    success_url = reverse_lazy('login')


