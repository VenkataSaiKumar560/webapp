from django.shortcuts import render,redirect
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
		usertype = request.POST['kind']
		if usertype=='Student':
			obj = Register(RID = userid,Name = username,Email=usermail,Phone=userphone,Password=userpwd,Stype=usertype)
			obj.save()
			return redirect('show')
		else:
			obj = Faculty(FID = userid,FName = username,FEmail=usermail,FPhone=userphone,FPassword=userpwd,Ftype=usertype)
			obj.save()
			return redirect('fshow')
		




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
		data1 = Faculty.objects.all()
		l1=[]
		k1=[]
		for i in data1:
			l1.append(i.FID)
			k1.append(i.FPassword)

		if urid in l and upwd in k:
			obj1 = Register.objects.get(RID=urid)
			sm = Studentmarks.objects.get(RgID=urid)
			return render(request,'myapp/details.html',{'data':obj1,'smks':sm})
			return HttpResponse("Valid User")
		

		elif urid in l and upwd not in k:
			return HttpResponse("Wrong Password,Please try again 1!")

		else:
			if urid in l1 and upwd in k1:
				obj = Faculty.objects.get(FID=urid)
				
				return render(request,'myapp/fdetails.html',{'data':obj})
				return HttpResponse("Valid User")
			elif urid in l1 and upwd not in k1:
				return HttpResponse("Wrong Password,Please try again 2!")
			else:
				return HttpResponse("Invalid User")


	return render(request,'myapp/login.html')

def edit(request,num,type1):
	if type1 == 'Student':
		obj = Register.objects.get(RID=num)
		obj2 = Studentmarks.objects.get(RgID=num)
		if request.method=='POST':
			obj.RID = request.POST['rid']
			obj.Name = request.POST['name']
			obj.Email = request.POST['mail']
			obj.Phone = request.POST['phone']
			obj.Password = request.POST['pass']
			obj.save()
			return render(request,'myapp/details.html',{'data':obj,'smks':obj2})
		return render(request,'myapp/update.html',{'data':obj})
	else:
		obj1 = Faculty.objects.get(FID=num)
		if request.method=='POST':
			obj1.FID = request.POST['rid']
			obj1.FName = request.POST['name']
			obj1.FEmail = request.POST['mail']
			obj1.FPhone = request.POST['phone']
			obj1.FPassword = request.POST['pass']
			obj1.save()
			return render(request,'myapp/fdetails.html',{'data':obj1})
		return render(request,'myapp/update.html',{'data':obj1})


def fshow(request):
	data = Faculty.objects.all()
	return render(request,'myapp/fdata.html',{'data':data})

def fmodify(request):
	if request.method=='POST':
		FacName = request.POST['fname']
		sid = request.POST['rid']
		smarks = request.POST['marks']
		atperc = request.POST['attend']
		obj = Studentmarks(Fname=FacName,RgID=sid,Marks=smarks,Attendance=atperc)
		obj.save()
		return HttpResponse("Modification Done")

	return render(request,'myapp/fmodf.html')