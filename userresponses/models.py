from django.db import models
from account.models import Users
from questionres.models import Questions
class UserResponses(models.Model):

	uid = models.ForeignKey(Users,on_delete=models.CASCADE)
	qid = models.ForeignKey(Questions,on_delete=models.CASCADE,null=False)
	uresponse = models.CharField(max_length=50)

	def __str__(self):
		return str(self.uid)+" - "+self.qid +" "+sef.uresponse[0:5]

	class Meta:
		db_table = "user_responses"
# Create your models here.
