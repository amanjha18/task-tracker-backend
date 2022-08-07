from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/team', views.create_team.as_view(), name='create-team'),
    path('create/task', views.create_task.as_view(), name='create-task'),
    path('update/task', views.UpdateTask.as_view(), name='update-task'),
    path('update/task/status', views.UpdateTaskStatus.as_view(), name='update-task-status'),
    path('list/task', views.ListTask.as_view(), name='list-task'),

]