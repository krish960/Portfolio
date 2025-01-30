from django.shortcuts import render
from anmins import models


# Create your views here.

def index(req):
	Data = models.IMAGES.objects.all()
	about=models.ABOUT.objects.all()
	about_mes=models.ABOUT_ME.objects.all()
	about_info = models.ABOUT_INFO.objects.all()
	Resumes=models.RESUME.objects.all()
	experience=models.EXPERENCE.objects.all()
	Educations=models.EDUCATIONS.objects.all()
	projects=models.PROJECT.objects.all()
	obj ={"Data": Data,"about": about,"about_mes": about_mes,"about_info":about_info,"Resumes": Resumes,"experience":experience,"Educations":Educations,"projects":projects}
	return render(req,"index.html",obj)