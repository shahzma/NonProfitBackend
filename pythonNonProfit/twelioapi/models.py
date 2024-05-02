from django.db import models

class Nonprofit(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(unique=True)

class Foundation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True)

class EmailRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    nonprofit = models.ForeignKey(Nonprofit, on_delete=models.CASCADE, default=1)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
