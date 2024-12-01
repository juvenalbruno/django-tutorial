from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)  # Exemplo de campo adicional

class Task(models.Model):
    name = models.CharField(max_length=50)
    task_list = models.ForeignKey("users.TaskList", on_delete=models.CASCADE, null=True, related_name="tasks")

class TaskList(models.Model):
    name = models.CharField(max_length=50)
