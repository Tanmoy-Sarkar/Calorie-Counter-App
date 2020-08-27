from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Food(models.Model):
	name = models.CharField(max_length=200 ,null=False)
	quantity = models.IntegerField(null=False,default=0)
	calorie = models.FloatField(null=False,default=0)
	person_of = models.ForeignKey(User,null=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Profile(models.Model):
	person_of = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	calorie_count = models.FloatField(null=True,blank=True,default=0)
	food_selected = models.ForeignKey(Food,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)

	def save(self, *args, **kwargs):# new
		self.amount = self.food_selected.calorie  
		self.calorie_count = self.amount*self.quantity     
		super(Profile, self).save(*args,**kwargs)


	def __str__(self):
		return self.person_of.username

