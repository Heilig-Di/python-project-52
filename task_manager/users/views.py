from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import ProtectedError
from django.contrib import messages


class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'

class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('Пользователь успешно зарегистрирован')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:list')
    success_message = _('Пользователь успешно изменен')

class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:list')
    success_message = _('Пользователь успешно удален')

    def get(self, request, *args, **kwargs):
        user_to_delete = self.get_object()
        current_user = request.user

        if user_to_delete != current_user:
            messages.error(request, _('У вас нет прав для изменения другого пользователя.'))
            return redirect(self.success_url)
        if user_to_delete.task_set.exists():
            messages.error(request, _('Невозможно удалить пользователя, потому что он используется в задачах'))
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, _('Пользователь успешно удален'))
        return response
