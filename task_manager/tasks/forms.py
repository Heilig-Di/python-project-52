from django import forms
from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        widgets = {
            'labels': forms.SelectMultiple(),
        }

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super().__init__(*args, **kwargs)
            self.fields['executor'].queryset = User.objects.all()
            self.fields['status'].queryset = Status.objects.all()


