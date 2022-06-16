from django.urls import path

from .views import visits_view, api_view, user, users_all, notes_handler, json_handler

urlpatterns = [
    path('', api_view, name="api_view"),
    path('visits/', visits_view, name="visits_view"),
    path('users/', user),
    path('users/all', users_all),
    path('assets/audio/<str:path>', notes_handler),
    path('assets/json/<str:path>', json_handler),
]