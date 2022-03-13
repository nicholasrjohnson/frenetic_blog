from re import template
from time import time
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import datetime
from django.db.models import Max, Count
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from .models import Author
from .forms import RegistrationForm

class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs) 
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('accounts:login')
        if next_url:
            success_url += '?next={}'.format(next_url)
            
        return success_url

class ProfileView(UpdateView):
    model = Author
    fields = ['name', 'phone', 'date_of_birth', 'photo', 'bio', 'signature']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('blog:index')
    
    def get_object(self):
        return self.request.user
