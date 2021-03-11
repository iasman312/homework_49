from django.urls import path

from webapp.views import IndexView, TaskView, TaskCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/', TaskView.as_view(), name='task-view'),
]