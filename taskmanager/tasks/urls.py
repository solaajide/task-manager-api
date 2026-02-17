from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='tasks'),
    path('tasks/<int:id>/', views.TaskRetrieveUpdateDeleteView.as_view(), name='task')
]