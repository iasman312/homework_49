from django.views.generic import UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin

from webapp.forms import UserForm
from webapp.models import Project


class ProjectUserAdd(PermissionRequiredMixin, UpdateView):
    template_name = 'users/add.html'
    form_class = UserForm
    model = Project
    permission_required = 'webapp.add_or_delete_user'

    def get_success_url(self):
        return reverse(
            'webapp:project-view',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def has_permission(self):
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in project.user.all()


