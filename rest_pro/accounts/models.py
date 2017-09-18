from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Expense(models.Model):
    category = models.CharField(max_length=64,blank=True,null=False)
    price = models.IntegerField(blank=True,null=False)
    description = models.TextField(max_length=128,blank=True,null=False)
    user = models.ForeignKey(User)
