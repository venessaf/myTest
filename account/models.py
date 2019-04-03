from django.db import models

class Users(models.Model):
	uid = models.AutoField(primary_key=True)
	eid = models.CharField(unique=True,max_length=10)
	fname = models.CharField(max_length=15)
	lname = models.CharField(max_length=15)
	email = models.EmailField()

	def __str__(self):
		return  self.fname+"  "+self.lname+" - "+self.eid

	class Meta:
		db_table = "users"
# Create your models here.
