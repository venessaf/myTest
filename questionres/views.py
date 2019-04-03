from django.shortcuts import render
from django.shortcuts import render,redirect
from questionres.models import Questions
from questionres.models import Responses

from userresponses.models import UserResponses
from questionres.forms import QuestionsForm


def quedemo(request):
	return render(request,'que.html')


def allQuestions(request):
	questions = Questions.objects.all()
	return render(request,'questiontable.html',{"questions":questions})
	pass

def questionEdit(request,id):
	question = Questions.objects.get(qid=id)
	return render(request,"question_update.html",{'question':question})

def questionUpdate(request,id):
	question = Questions.objects.get(qid=id)
	form = QuestionsForm(request.POST,instance=question)

    # all the Responses of Questions whose qid =id
	res1 = Responses.objects.filter(qid=id)

	if form.is_valid:
		# -------------- Update the Response Table -------------

		#  if Not any Change in the Options
		updated_question_options = str(form['options'].value())
		old_question_options = str(question.options)
		if updated_question_options == old_question_options:
			pass
		else:
			updated_question_options = updated_question_options.split(",")
			for opt in updated_question_options:
				# If Response already exist
				if opt in old_question_options:
					pass
				# If options already not there add it
				else:
					response1 = Responses()
					response1.response = opt
					response1.qid = question
					response1.save()

		# -----------------------------------------------------
		form.save()
		return redirect('/question/all')

	return render(request,"question_update.html",{'question':question})

def questionDelete(request,id):
	question = Questions.objects.get(qid=id)
	question.delete()
	return redirect('/question/all')

def questionDetail(request,id):

	question = Questions.objects.get(qid=id)
	res_to_question = UserResponses.objects.filter(qid=id)
	return render(request,"question_detail.html",{'count':res_to_question.count(),'res_to_question':res_to_question,'que':question})


def addQuestion(request):

	myqid =" "
	question_options = []


	if request.method=="POST":
		form = QuestionsForm(request.POST)
		if form.is_valid():
			try:
				# Fill Data In Responses Table
				form.save()
				# print(form)
				que1 = form['question'].value()
				que1 = Questions.objects.get(question=que1)
				print(que1)
				response1 = Responses()

				# ------------------ QID ----------------------------

				 # myqid = form['qid'].value()

				# ----------------- Responses -----------------------

				question_options = form['options'].value()
				# print(question_options)
				question_options =  question_options.split(",")
				# print(question_options)
				for opt in question_options	:
					response1 = Responses()
					response1.response = opt
					response1.qid = que1
					response1.save()
					print(opt)


				# ------------------ Rid AutoIncrement ------------------


				return redirect('/question/all')
			except Exception as e:
				raise
	else:
		form= QuestionsForm()
	return render(request,"question_form.html",{'form':form})

# Create your views here.
