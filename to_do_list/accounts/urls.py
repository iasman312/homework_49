from django.urls import path
from accounts.views import register_view, UserDetailView, UserList, UserChangeView, UserPasswordChangeView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change')
]

