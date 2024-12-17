from django.db import models
# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    smtp_server = models.CharField(max_length=100)
    smtp_email = models.CharField(max_length=100)
    smtp_password = models.CharField(max_length=100)
    smtp_port = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    icon = models.ImageField(null=False, upload_to='images/settings/')
    about_us = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
  
