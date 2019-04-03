from django.shortcuts import render,redirect
from account.models import Users
from userresponses.models import UserResponses
from account.forms import UsersForm
def accdemo(request):
	return render(request,'acc.html')
# Create your views here.

def allUsers(request):
	employees = Users.objects.all()
	return render(request,'usertable.html',{"employees":employees})

def userEdit(request,id):
	employee = Users.objects.get(uid=id)
	return render(request,"employee_update.html",{'employee':employee})

def userUpdate(request,id):
	employee = Users.objects.get(uid=id)
	form = UsersForm(request.POST,instance=employee)
	if form.is_valid:
		form.save()
		return redirect('/employee/all')

	return render(request,"employee_update.html",{'employee':employee})

def userDelete(request,id):
	employee = Users.objects.get(uid=id)
	employee.delete()
	return redirect('/employee/all')

def userDetail(request,id):
	res_of_user = UserResponses.objects.filter(uid=id)
	useri = Users.objects.get(uid=id)
	return render(request,"employee_detail.html",{'res_of_user':res_of_user,'user':useri,'count':res_of_user.count()})


def addUser(request):

	if request.method=="POST":
		form = UsersForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/employee/all')
			except Exception as e:
				raise
	else:
		form= UsersForm()
	return render(request,"employee_form.html",{'form':form})

	pass