from django.db import models
from django import forms
class Questions(models.Model):
	qid = models.AutoField(primary_key=True)
	question = models.TextField()

	isMcq = models.BooleanField(default=True,blank=True)
	options = models.CharField(max_length=50) 

	def __str__(self):
		return str(self.qid)+" -  "+self.question[0:12]

	class Meta:
		db_table= "questions"
		# app_label = "questions"	

class Responses(models.Model):
	resid = models.AutoField(primary_key=True)
	qid = models.ForeignKey(Questions,on_delete=models.CASCADE)		
	response = models.CharField(max_length=50)

	class Meta:
		db_table = "responses"

	def __str__(self):
		return str(self.qid)+" - "+self.response	

# Create your models here.
