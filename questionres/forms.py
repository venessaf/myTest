from django import forms
from questionres.models import Questions

class QuestionsForm(forms.ModelForm):

	question = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control demo'}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['question'].widget.attrs.update(cols='16',rows='3',
			placeholder="Enter the Question")
		# self.fields['question'].widget.attrs.update("class"='demo')
		# self.fields['question'].widget.attrs.update({"cols":20,"rows":7,
		# 	"placeholder":"Enter the Question","class":"form-control"})

		pass
	class Meta:
		model = Questions
		# fields ="__all__"
		fields =("isMcq","question","options","qid")
		# widgets = {

		# 	'question':forms.Textarea(attrs={'class':'form-control'})
		# }
