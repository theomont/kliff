from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

