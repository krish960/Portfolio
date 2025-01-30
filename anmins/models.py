from django.db import models

# Create your models here.

class IMAGES(models.Model):
	img = models.ImageField(upload_to='static/admin/img')

class ABOUT(models.Model):
	Name=models.CharField(max_length=100)
	Job_Role=models.CharField(max_length=100)
	Experience=models.CharField(max_length=100)
	Address=models.CharField(max_length=100)

class ABOUT_ME(models.Model):
	Desc=models.CharField(max_length=100)

class ABOUT_INFO(models.Model):
	Profile=models.CharField(max_length=100)
	Education=models.CharField(max_length=100)
	Language=models.CharField(max_length=100)
	Tools=models.CharField(max_length=100)
	O_Skills=models.CharField(max_length=100)
	Interest=models.CharField(max_length=100)
	Projects_completed=models.CharField(max_length=100)

class RESUME(models.Model):
	Resume_desc=models.CharField(max_length=100)
	Resume_link=models.CharField(max_length=100)

class EXPERENCE(models.Model):
	Years=models.CharField(max_length=100)
	Skill=models.CharField(max_length=100)
	Devlopment=models.CharField(max_length=100)
	heading=models.CharField(max_length=100)
	heading_info1=models.CharField(max_length=100)
	heading_info2=models.CharField(max_length=100)
	heading_info3=models.CharField(max_length=100)

class EDUCATIONS(models.Model):
	passing_year=models.CharField(max_length=100)
	Degree=models.CharField(max_length=100)
	University=models.CharField(max_length=100)
	Grade=models.CharField(max_length=100)

class PROJECT(models.Model):
	img_Projects = models.ImageField(upload_to='static/admin/img')
	Projects_Name=models.CharField(max_length=100)
	Projects_Info=models.CharField(max_length=100)
	Projects_Link=models.CharField(max_length=100)
