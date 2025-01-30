from django.shortcuts import render,redirect
from anmins import models

# Create your views here.

def home(req):
	return render(req,"admins/home.html")

def IMG(req):
	Data=models.IMAGES.objects.all()
	obj ={"Data": Data}
	return render(req,"admins/IMG.html",obj)

def delete_img(req):
	order_id = req.GET['id']
	models.IMAGES.objects.get(id = order_id).delete();
	return redirect("/admin/IMG")

def save_img(req):
	Data = models.IMAGES(
        img = req.FILES['img']
	)
	Data.save()
	return redirect("/admin/IMG")

def About(req):
	about=models.ABOUT.objects.all()
	obj ={"about": about}
	return render(req,"admins/About.html",obj)

def save_about(req):
	about=models.ABOUT(

		Name=req.POST['Name'],
		Job_Role=req.POST['Job_Role'],
		Experience=req.POST['Experience'],
		Address=req.POST['Address'],

	)
	about.save()
	return redirect("/admin/About")

def delete_rec(req):
	order_id = req.GET['id']
	models.ABOUT.objects.get(id = order_id).delete();
	return redirect("/admin/About")

def about_me(req):
	about_mes=models.ABOUT_ME.objects.all()
	obj ={"about_mes": about_mes}
	return render(req,"admins/about_me.html",obj)

def save_about_me(req):
	about_mes=models.ABOUT_ME(

		Desc=req.POST['Desc'],
	)
	about_mes.save()
	return redirect("/admin/about_me")

def delete_Desc(req):
	order_id = req.GET['id']
	models.ABOUT_ME.objects.get(id = order_id).delete();
	return redirect("/admin/about_me")

def About_info(req):
	about_info = models.ABOUT_INFO.objects.all()
	obj ={"about_info": about_info}
	return render(req,"admins/About_info.html",obj)

def save_about_info(req):
	about_info = models.ABOUT_INFO(
		Profile=req.POST['Profile'],
		Education=req.POST['Education'],
		Language=req.POST['Language'],
		Tools=req.POST['Tools'],
		O_Skills=req.POST['O_Skills'],
		Interest=req.POST['Interest'],
		Projects_completed=req.POST['Projects_completed'],
	)
	about_info.save()
	return redirect("/admin/About_info")

def delete_about_info(req):
	order_id = req.GET['id']
	models.ABOUT_INFO.objects.get(id = order_id).delete()
	return redirect("/admin/About_info")

def Resume(req):
	Resumes=models.RESUME.objects.all()
	obj ={"Resumes": Resumes}
	return render(req,"admins/Resume.html",obj)

def save_Resume_link(req):
	Resumes=models.RESUME(
		Resume_desc=req.POST['Resume_desc'],
		Resume_link=req.POST['Resume_link'],

	)
	Resumes.save()
	return redirect("/admin/Resume")

def delete_Resume(req):
	order_id = req.GET['id']
	models.RESUME.objects.get(id = order_id).delete()
	return redirect("/admin/Resume")

def Experience(req):
	experience=models.EXPERENCE.objects.all()
	obj ={"experience": experience}
	return render(req,"admins/Experience.html",obj)

def save_Experience(req):
	experience=models.EXPERENCE(
		Years=req.POST['Years'],
		Skill=req.POST['Skill'],
		Devlopment=req.POST['Devlopment'],
		heading=req.POST['heading'],
		heading_info1=req.POST['heading_info1'],
		heading_info2=req.POST['heading_info2'],
		heading_info3=req.POST['heading_info3'],
	)
	experience.save()
	return redirect("/admin/Experience")

def delete_experience(req):
	order_id = req.GET['id']
	models.EXPERENCE.objects.get(id = order_id).delete()
	return redirect("/admin/Experience")

def Education(req):
	Educations=models.EDUCATIONS.objects.all()
	obj ={"Educations": Educations}
	return render(req,"admins/Education.html",obj)

def save_Education(req):
	Educations=models.EDUCATIONS(
		passing_year=req.POST['passing_year'],
		Degree=req.POST['Degree'],
		University=req.POST['University'],
		Grade=req.POST['Grade'],
	)
	Educations.save()
	return redirect("/admin/Education")

def delete_Education(req):
	order_id=req.GET['id']
	models.EDUCATIONS.objects.get(id = order_id).delete()
	return redirect("/admin/Education")

def Projects(req):
	projects=models.PROJECT.objects.all()
	obj= {"projects": projects}
	return render(req,"admins/Projects.html",obj)

def save_Projects(req):
	projects=models.PROJECT(
        img_Projects = req.FILES['img_Projects'],
		Projects_Name=req.POST['Projects_Name'],
		Projects_Info=req.POST['Projects_Info'],
		Projects_Link=req.POST['Projects_Link']
	)		
	projects.save()
	return redirect("/admin/Projects")

def delete_Projects(req):
	order_id=req.GET['id']
	models.PROJECT.objects.get(id = order_id).delete()
	return redirect("/admin/Projects")