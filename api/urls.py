from django.urls import path

from .views import debug_view, visits_view, api_view, tasks, task_detail

urlpatterns = [
    path('', api_view, name="api_view"),
    path('test/', debug_view, name="test_view"),
    path('visits/', visits_view, name="visits_view"),
    path('tasks/', tasks),
    path('tasks/<int:pk>/', task_detail)
]