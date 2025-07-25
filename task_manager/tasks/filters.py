import django_filters
from .models import Task
from django import forms
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label="Статус",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label="Исполнитель",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label="Метка",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    self_tasks = django_filters.BooleanFilter(
        method='filter_self_tasks',
        label="Только свои задачи",
        widget=forms.CheckboxInput()
    )


    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'self_tasks']


    def filter_self_tasks(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(author=self.request.user)
        return queryset
