from django.db import models

# Create your models here.

class UrlModel(models.Model):
    url_id=models.AutoField(primary_key=True)
    url_link=models.CharField(max_length=1000000)
    short_link=models.CharField(max_length=1000000)
