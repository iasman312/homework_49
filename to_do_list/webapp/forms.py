from django import forms

from django.forms import widgets
from webapp.models import Status, Type, Task


class TaskForm(forms.ModelForm):
    summary = forms.CharField(max_length=120, required=True, label='Краткое '
                                                                   'описание')
    description = forms.CharField(max_length=1000, required=False,
                                  widget=widgets.Textarea, label='Полное '
                                                                 'описание')
    statuses = forms.ModelChoiceField(queryset=Status.objects.all())
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),
                                           widget=forms.CheckboxSelectMultiple)

