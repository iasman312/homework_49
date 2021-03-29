from django.urls import path

from webapp.views import (
    IndexView,
    ProjectView,
    ProjectCreateView,
    TaskCreateView,
    TaskView,
    TaskUpdateView,
    TaskDeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectView.as_view(), name='project-view'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/tasks/add/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskView.as_view(), name='task-view'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(),
         name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(),
         name='task-delete'),
]