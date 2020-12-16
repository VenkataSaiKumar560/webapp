from django.db import models

# Create your models here.
class Register(models.Model):
	RID = models.CharField(max_length=10,unique=True)
	Name = models.CharField(max_length=40)
	Email = models.EmailField(unique=True,null=True)
	Phone = models.CharField(max_length=10)
	Password = models.CharField(max_length=30)
	Stype = models.CharField(max_length=20,null=True)
	def __str__(self):
		return self.RID

class Faculty(models.Model):
	FID = models.CharField(max_length=30,unique=True)
	FName = models.CharField(max_length=40)
	FEmail = models.EmailField(unique=True,null=True)
	FPhone = models.CharField(max_length=10)
	FPassword = models.CharField(max_length=30)
	Ftype = models.CharField(max_length=20,null=True)
	def __str__(self):
		return self.FID

class Studentmarks(models.Model):
	Fname = models.CharField(max_length=20)
	RgID = models.CharField(max_length=20,unique=True)
	Marks = models.CharField(max_length=10)
	Attendance = models.CharField(max_length=10)
	def __str__(self):
		return self.Fname + " " + self.RdID