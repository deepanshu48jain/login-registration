from django.db import models


class UserDetails(models.Model):
	username = models.CharField(max_length=100)
	email = models.EmailField(max_length=250)
	password = models.CharField(max_length=50)
	mobile_no = models.IntegerField()
	image = models.ImageField()

	def __str__(self):
		return self.username