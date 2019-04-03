from django import forms
from account.models import Users

class UsersForm(forms.ModelForm):
	class Meta:
		model = Users
		# fields ="__all__"
		fields =("eid","fname","lname","email")

		