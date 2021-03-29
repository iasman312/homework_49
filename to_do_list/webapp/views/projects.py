from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, RedirectView, FormView, \
    ListView, DetailView
from django.urls import reverse
from django.db.models import Q
from django.utils.http import urlencode

from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task, Project


class IndexView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'projects/index.html'
    paginate_by = 3
    paginate_orphans = 1


class ProjectView(DetailView):
    template_name = 'projects/view.html'
    model = Project
