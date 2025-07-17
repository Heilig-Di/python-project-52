from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {
            "name": "Имя",
            "description": "Описание",
            "status": "Статус",
            "executor": "Исполнитель",
            "labels": "Метки",
        }
        widgets = {
            'labels': forms.Textarea(attrs={'rows': 4}),
        }

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super().__init__(*args, **kwargs)
            self.fields['executor'].queryset = User.objects.all()
            self.fields['status'].queryset = Status.objects.all()
