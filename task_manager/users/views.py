from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from .models import User
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserUpdateForm, LoginForm
from django.contrib.auth import login, logout


class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:list')

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class LogoutView(FormView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')
