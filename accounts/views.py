from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,CreateView
from .forms import CustomUserCreationForm   
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"

    success_url = reverse_lazy('accounts:signup_success')
    def form_valid(self,form):
        user = form.save()
        self.object = user
        return super().form_valid(form)
    
class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"

class LoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy('accounts:login')