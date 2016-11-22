#from django.http import HttpResponse
#from django.shortcuts import render_to_response
from .forms import *
from .models import models
from django.http import *
from django.shortcuts import *
#from django.contrib.auth.models import User, Group
import random
from django.contrib.auth.decorators import login_required



def home(request):
    return render_to_response('TestProject/home.html')

def register(request):
    return render_to_response('registration/registration_form.html')

def login_page(request):
    return render_to_response('registration/login.html')

def logout_page(request):
    return render_to_response('registration/logout.html')

def registration_closed(request):
    return render_to_response('registration/registration_closed.html')

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')


def error404(request):
	return render(request,"TestProject/404.html")


def PrimerTests(HttpRequest):
	try:
		tests = Test.objects.values("Name", "DateActivate", "Time")
	except:
		return HttpResponseServerError("Server error")
	return render(HttpRequest, "TestProject/tests.html",{"tests": tests})

@login_required(login_url='/accounts/login/')
def TestsUser(request):
	subscribe = TestPerson.objects.filter(Person = request.user.id)
	with_mark = []
	without_mark = []
	for sub in subscribe:
		if sub.get_mark() != None:
			with_mark.append(sub)
		else:
			without_mark.append(sub)
	return render(request,"TestProject/profile.html",
                  {
					  "completed_tests":with_mark, "uncompleted_tests":without_mark
                  })

def AddUsers(request):
	if request.user.is_superuser:
		if (request.method == "POST"):
			Groups = request.POST['Group']
			group = GP(NameGP = Groups)
			group.save()
			users = request.POST['users']
			users = users.split('\n')
			count = 0
			for i in users:

				user = i.split(' ')

				person =MyUser.objects.create_user(
					username = Groups + str(count),
					email =None,
					password = 'Qwerty123'+ str(count),
					last_name = user[0],
					first_name = user[1],
					GP = group
				)
				count+=1
				person.save()
			return redirect("/admin")
		else:
			return render(request, "admin/generate_users.html")
	else:
		return redirect("/404")


def CreateTest(request):
	if request.user.is_superuser:
		if (request.method == "POST"):
			form = TestForm(request.POST)
			task = Task.objects.all()
			taskId = []
			for i in task:
				taskId.append(i.id)

			i = 0
			if form.is_valid():
				test = Test(
					Name = form.cleaned_data['Name'],
					DateActivate =form.cleaned_data['DateActivate'],
					Time = form.cleaned_data['Time']
				)
				test.save()
				connectdatabase = TestConnectDataBase(Test = test, ConnectDataBase = form.cleaned_data['ConnectDataBase'])
				connectdatabase.save()
				for i in range(form.cleaned_data['Variants']):
					tasks = []
					count = 0
					while count!=10:
						RandomId = random.choice(taskId)
						Check = RandomId in tasks
						if Check == False:
							tasks.append(RandomId)
							test_task = TestTask.objects.create(Test = test, Task = task.get(id = RandomId),Variant=i+1)
							count+=1
				return redirect("/admin")
		else:
			form = TestForm()

			"""Get categories and count of tasks in him"""
			category = Category.objects.all()
			tasks = Task.objects.all()
			dict = {}
			count = 0
			for i in category:
				dict[i.Name] = len(tasks.filter(Category=i))

			return render(request, 'admin/create_test.html', {'form': form,
															  'categoties': dict
														  })
	else:
		return redirect("/404")


