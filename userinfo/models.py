from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime
from datetime import datetime

class Usersdata(models.Model):
	id = models.AutoField(primary_key=True,max_length=11) 
	user_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=40)
	created_datetime = models.DateTimeField()
	location = models.CharField(max_length=40)
	attempts = models.IntegerField() 
	attempts_datetime = models.DateTimeField()
	class Meta:
		managed = False
		db_table = 'users_data'