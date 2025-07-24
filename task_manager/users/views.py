from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.messages.views import SuccessMessageMixin


class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('Пользователь успешно зарегистрирован')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:list')

