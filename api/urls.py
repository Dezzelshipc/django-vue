from django.urls import path

from .views import send_score, user, users_all, notes_handler, json_handler, username_data, send_score
urlpatterns = [
    path('users/', user),
    path('users/all', users_all),
    path('users/<str:username>', username_data),
    path('assets/audio/<str:path>', notes_handler),
    path('assets/json/<str:path>', json_handler),
    path('sendscore/<str:username>', send_score)
]