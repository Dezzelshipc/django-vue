from django.urls import path

from .views import visits_view, api_view, user, users_all, notes_handler, notes_player

urlpatterns = [
    path('', api_view, name="api_view"),
    path('visits/', visits_view, name="visits_view"),
    path('users/', user),
    path('users/all', users_all),
    path('notes/1/<str:note>', notes_handler),
    path('notes/<str:note>', notes_player),
]