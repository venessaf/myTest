from django.shortcuts import render
from django.shortcuts import render
from userresponses.models import UserResponses
def uresdemo(request):
	return render(request,'res.html')

def allResponses(request):
	responses = UserResponses.objects.all()
	return render(request,'responsestable.html',{"responses":responses})	
# Create your views here.
