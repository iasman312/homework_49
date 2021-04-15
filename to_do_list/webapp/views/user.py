from django.views.generic import UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from webapp.forms import UserForm
from webapp.models import Project


class ProjectUserAdd(LoginRequiredMixin, UpdateView):
    template_name = 'users/add.html'
    form_class = UserForm
    model = Project

    def get_success_url(self):
        return reverse(
            'webapp:project-view',
            kwargs={'pk': self.kwargs.get('pk')}
        )


