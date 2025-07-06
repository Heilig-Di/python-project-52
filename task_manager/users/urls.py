from django.urls import path

from task_manager.users import views


urlpatterns = [
    path("create/", UserCreateView.as_view(), name="create"),
    path("list/", UserListView.as_view(), name="list"),
    path("update/", UserUpdateView.as_view(), name="update"),
    path("delete/", UserDeleteView.as_view(), name="delete")
]
