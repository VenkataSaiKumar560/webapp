from django.db import models

# Create your models here.
class Register(models.Model):
	RID = models.CharField(max_length=10)
	Name = models.CharField(max_length=40)
	Email = models.EmailField(null=True,blank=True)
	Phone = models.CharField(max_length=10)
	Password = models.CharField(max_length=30)
	def __str__(self):
		return self.RID