from email.policy import default
from django.db import models

def default_data():
    return {
        "bestSpeed": 0.0,
        "random": 
            {"bestSpeed": 0.0, "last":[]},
        "text":
            {"bestSpeed": 0.0, "last":[]}
    }

class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    telegram = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    data = models.JSONField(default=default_data)

    def __str__(self):
        return self.username
