from django.db import models
from rest_framework.fields import timezone



class EmailModel(models.Model):

    name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=False, unique=True)
    message = models.TextField(max_length=500)
    contact_date = models.DateTimeField(default=timezone.now, blank=True)



    def __str__(self):
        return self.email
