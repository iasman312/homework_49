from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, \
    ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode

from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task, Project


class TasksView(ListView):
    template_name = 'index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(
                description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class TaskView(TemplateView):
    template_name = 'tasks/view.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)


class TaskCreateView(CreateView):
    template_name = 'tasks/create.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse(
            'project-view',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        project = get_object_or_404(Project, id=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.project.pk})


class TaskDeleteView(DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.project.pk})
