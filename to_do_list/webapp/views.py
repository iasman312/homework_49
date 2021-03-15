from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView

from webapp.forms import TaskForm
from webapp.models import Task


class TaskRedirectView(RedirectView):
    pattern_name = 'task-view'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['tasks'] = Task.objects.all()
        return super().get_context_data(**kwargs)


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)


class TaskCreateView(TemplateView):
    template_name = 'task_create.html'

    def get_context_data(self, **kwargs):
        kwargs['form'] = TaskForm()
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            task = Task.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status'))
            task.types.set(types)
            return redirect('task-view', pk=task.id)
        kwargs['form'] = form
        return super().get_context_data(**kwargs)


class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'types': task.types.all()
        })
        kwargs['form'] = form
        kwargs['task'] = task
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data.get('summary')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            types = form.cleaned_data.pop('types')
            task.save()
            task.types.set(types)
            return redirect('task-view', pk=task.id)

        kwargs['form'] = form
        kwargs['task'] = task
        return super().get_context_data(**kwargs)


class TaskDeleteView(TemplateView):
    template_name = 'task_delete.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('pk'))
        task.delete()
        return redirect('task-list')



