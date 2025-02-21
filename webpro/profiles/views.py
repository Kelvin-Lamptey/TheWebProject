from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'profiles/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')  # Change 'home' to your desired redirect URL

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'profiles/register.html'
    success_url = reverse_lazy('home')  # Change 'home' to your desired redirect URL

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
