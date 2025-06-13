from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    services = models.JSONField()
    logo = models.ImageField(upload_to="logos/")
    drive_connected = models.BooleanField(default=False)
    dropbox_connected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
