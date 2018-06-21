from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime
from datetime import datetime
from userinfo.models import Usersdata 

class Userssession(models.Model):
	id = models.AutoField(primary_key=True,max_length=11) 
	user = models.ForeignKey(Usersdata)
	sessionkey = models.CharField(max_length=32)
	class Meta:
		managed = False
		db_table = 'users_session'




