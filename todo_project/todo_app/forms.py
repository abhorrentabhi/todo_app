from .models import Task
from django import forms


class todo_forms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']
