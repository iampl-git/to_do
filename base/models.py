from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name
