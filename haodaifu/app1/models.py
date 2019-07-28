from django.db import models

# Create your models here.

class answer(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

class content(models.Model):
    detail = models.CharField(max_length=255)
    con = models.ForeignKey(answer,on_delete=models.SET_NULL,null=True)