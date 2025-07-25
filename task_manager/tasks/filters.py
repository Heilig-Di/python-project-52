import django_filters
from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Статус',
        field_name='status'
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Исполнитель',
        field_name='executor'
    )
    label = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка',
        field_name='label'
    )

    self_tasks = django_filters.BooleanFilter(
        field_name='author',
        method='filter_self_tasks',
        label='Только свои задачи',
        widget=django_filters.widgets.BooleanWidget
    )


    class Meta:
        model = Task
        fields = ['status', 'executor', 'label']


    def filter_self_tasks(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(author=self.request.user)
        return queryset
