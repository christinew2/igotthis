from django.db import models
from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length = 100)
    details = models.TextField(max_length = 250)
    is_priority = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self-NameError

    # def get_absolute_url(self):
    #     return reverse("todos_detail", kwargs={"todo_id": self.id})
    
