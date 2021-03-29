from django.urls import path

from webapp.views import (
    IndexView,
    ProjectView,
    ProjectCreateView
    # TaskView,
    # TaskCreateView,
    # TaskUpdateView,
    # TaskDeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectView.as_view(), name='project-view'),
    path('create/', ProjectCreateView.as_view(), name='project-create')
    # path('create/', TaskCreateView.as_view(), name='task-create'),
    # path('<int:pk>/', TaskView.as_view(), name='task-view'),
    # path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    # path('<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
]