from django.urls import path

from .views import user, users_all, notes_handler, json_handler, username_data

urlpatterns = [
    path('users/', user),
    path('users/all', users_all),
    path('users/<str:username>', username_data),
    path('assets/audio/<str:path>', notes_handler),
    path('assets/json/<str:path>', json_handler),
]