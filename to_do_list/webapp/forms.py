from django import forms

from django.forms import widgets
from webapp.models import Task, Type


class TaskForm(forms.ModelForm):
    types = forms.ModelMultipleChoiceField(required=False, label='Типы',
                                           queryset=Type.objects.all(),
                                           widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = ['summary', 'description', 'statuses', 'types']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")