from django.db import models
from django.utils import timezone
# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=150)
    task=models.TextField()
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
