from django import forms

from django.forms import widgets
from webapp.models import Task, Type, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'finish_date']


class TaskForm(forms.ModelForm):
    types = forms.ModelMultipleChoiceField(required=False, label='Типы',
                                           queryset=Type.objects.all(),
                                           widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = ['summary', 'description', 'statuses', 'types']


class UserForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['user',]


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


