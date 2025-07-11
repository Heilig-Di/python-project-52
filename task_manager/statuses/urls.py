from django.urls import path
from task_manager.users.views import (
    StatusCreateView,
    StatusListView,
    StatusUpdateView,
    StatusDeleteView
)

app_name = 'statuses'

urlpatterns = [
    path("create/", StatusCreateView.as_view(), name="create"),
    path("", StatusListView.as_view(), name="list"),
    path("<int:pk>/update/", StatusUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", StatusDeleteView.as_view(), name="delete")
]
