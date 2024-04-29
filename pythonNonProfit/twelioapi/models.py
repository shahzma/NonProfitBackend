from django.db import models

class Nonprofit(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(unique=True)

class Foundation(models.Model):
    email = models.EmailField(unique=True)

class EmailRecord(models.Model):
    recipient_email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
