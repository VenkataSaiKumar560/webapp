from django.shortcuts import render
from django.http import *
from .models import *


# Create your views here.
def register(request):
	if request.method == 'POST':
		userid = request.POST['rid']
		username = request.POST['name']
		usermail = request.POST['mail']
		userphone = request.POST['phone']
		userpwd = request.POST['pass']
		obj = Register(RID = userid,Name = username,Email=usermail,Phone=userphone,Password=userpwd)
		obj.save()
		data = Register.objects.all()
		return render(request,'myapp/data.html',{'data':data})




	return render(request,'myapp/register.html')

def show(request):
	data = Register.objects.all()
	return render(request,'myapp/data.html',{'data':data})

def home(request):
	return render(request,'myapp/home.html')

def login(request):
	if request.method =='POST':
		urid = request.POST['rid']
		upwd = request.POST['pass']
		data = Register.objects.all()
		l=[]
		k=[]
		for i in data:
			l.append(i.RID)
			k.append(i.Password)

		if urid in l and upwd in k:
			return HttpResponse("Valid User")
		

		elif urid in l and upwd not in k:
			return HttpResponse("Wrong Password,Please try again!")

		else:
			return HttpResponse("Invalid User")


		
		



	return render(request,'myapp/login.html')