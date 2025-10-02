from django.shortcuts import render
from .forms import TestForm, CustomLoginForm, CustomUserForm
from django.views.generic import (
    CreateView,
    UpdateView, 
    ListView, 
    DetailView
)
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
class CustomSignupView(CreateView):
    form_class = CustomUserForm
    template_name = "modelform/signup.html"
    success_url = reverse_lazy("modelform:index")
 

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "modelform/login.html"
    success_url = reverse_lazy("modelform:index")

def index(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            form = TestForm()
            return render(request, 'modelform/index.html', {'form': form})
        return render(request, 'modelform/index.html', {'form': form})
    
    return render(request, 'modelform/index.html', {'form': form})