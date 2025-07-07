from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User

# Create your views here.
class UserListView(ListView):
    model = User
    template_name = 'users/list.html'

class UserCreateView(CreateView):
    model = User
    template_name = 'users/create.html'

class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/update.html'

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
