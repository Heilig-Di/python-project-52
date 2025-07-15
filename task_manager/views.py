from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from task_manager.users.forms import LoginForm


class HomeView(TemplateView):
    template_name = "index.html"

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')

class LogoutView(FormView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')
