from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Create table model for Users

#Gear class as example of ForeignKey relation between tables for later
#class gear(models.Model):
#	gear_item=models.CharField(max_lenght=100)
#	gear_class=models.CharField(max_length=50)
#	gear_owner=models.ForeignKey(User, on_delete=models.CASCADE)


class trails(models.Model):
	trail_name=models.TextField()
	popularity=models.FloatField()
	lat=models.FloatField()
	lng=models.FloatField()
	length=models.FloatField()
	elevation_gain=models.FloatField()
	difficulty=models.IntegerField()
	trail_type=models.CharField(max_length=2)
	area_name=models.CharField(max_length=250)
	city_id=models.IntegerField()
	city_name=models.CharField(max_length=150)
	state_id=models.IntegerField()
	state_name=models.CharField(max_length=50)
	url=models.SlugField(max_length=1000)


