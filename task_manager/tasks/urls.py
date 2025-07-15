from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView
)

app_name = 'tasks'

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create'),
    path('', TaskListView.as_view(), name='list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
]
