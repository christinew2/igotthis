from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Todo(models.Model):
    name = models.CharField(max_length = 100)
    details = models.TextField(max_length = 250, blank=True)
    is_priority = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

