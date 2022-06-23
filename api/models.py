from django.db import models

class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    telegram = models.CharField(max_length=128, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    bestSpeed = models.FloatField(default=0)

    def __str__(self):
        return self.username
