from django.urls import path
from task_manager.users.views import (
    UserCreateView,
    UserListView,
    UserUpdateView,
    UserDeleteView
)

app_name = 'users'

urlpatterns = [
    path("create/", UserCreateView.as_view(), name="create"),
    path("", UserListView.as_view(), name="list"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="delete")
]
