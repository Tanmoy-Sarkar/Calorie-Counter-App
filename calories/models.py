from django.db import models

# Create your models here.

class Food(models.Model):
	name = models.CharField(max_length=200 ,null=False)
	calorie = models.FloatField(null=False)