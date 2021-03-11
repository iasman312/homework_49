from django import forms

from django.forms import widgets
from webapp.models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=120, required=True, label='Краткое '
                                                                   'описание')
    description = forms.CharField(max_length=1000, required=False,
                                  widget=widgets.Textarea, label='Полное '
                                                                 'описание')
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelChoiceField(queryset=Type.objects.all())

