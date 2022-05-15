from django.urls import path

from .views import debug_view, visits_view

urlpatterns = [
    path(r'^test/$', debug_view, name="test_view"),
    path(r'^visits/$', visits_view, name="visits_view")
]