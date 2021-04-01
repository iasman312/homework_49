from django.urls import path

from webapp.views import (
    IndexView,
    ProjectView,
    ProjectCreateView,
    TaskCreateView,
    TaskView,
    TaskUpdateView,
    TaskDeleteView,
    ProjectUpdateView,
    ProjectDeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectView.as_view(), name='project-view'),
    path('<int:pk>/update', ProjectUpdateView.as_view(), name='project-update'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(),
         name='project-delete'),
    path('<int:pk>/tasks/add/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskView.as_view(), name='task-view'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(),
         name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(),
         name='task-delete'),
]