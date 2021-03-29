from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse

from webapp.forms import ProjectForm
from webapp.models import Project


class IndexView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'projects/index.html'
    paginate_by = 3
    paginate_orphans = 1


class ProjectView(DetailView):
    template_name = 'projects/view.html'
    model = Project
    context_object_name = "project"


class ProjectCreateView(CreateView):
    template_name = 'projects/create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.pk})
