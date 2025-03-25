from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    domain = models.TextField(blank=True)
    webpage = models.URLField()

    def __str__(self):
        return self.name
