from django.db import models

# Create your models here.
# Database ----> Excel workbook
# Table ----->sheet

class Contact (models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
          return "Message from " + self.name + ' - ' + self.email
