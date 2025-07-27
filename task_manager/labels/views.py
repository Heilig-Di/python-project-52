from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Label
from .forms import LabelForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/list.html'
    context_object_name = "labels"


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('Метка успешно создана')


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('Метка успешно изменена')


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('Метка успешно удалена')
    error_message = _('Невозможно удалить метку, потому что она используется')

    def post(self, request, *args, **kwargs):
        label = self.get_object()

        if label.tasks.exists():
            messages.error(request, self.error_message)
            return redirect(self.success_url)
        try:
            label.delete()
            messages.success(request, self.success_message)
            return redirect(self.success_url)
        except Exception as e:
            messages.error(request, str(e))
            return redirect(self.success_url)
