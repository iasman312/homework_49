from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404

from webapp.forms import ProjectForm
from webapp.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'projects/index.html'
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(is_deleted=False)


class ProjectView(DetailView):
    template_name = 'projects/view.html'
    model = Project
    context_object_name = "project"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_deleted == True:
            raise Http404
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'projects/delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        return super().post(request, *args, **kwargs)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, pk=pk)

