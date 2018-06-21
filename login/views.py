from django.shortcuts import render
import hashlib

# Create your views here.
from userinfo.models import Usersdata
from django.http import HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.conf import settings
from datetime import datetime
from django.db.models import Sum
from login.models import Userssession
from django.db.models import F
from django.utils import timezone
def login(request):
	if request.method == 'POST':
		email= (request.POST.get('email')).strip()
		password = hashlib.md5((request.POST.get('password')).strip()).hexdigest()
		
		check = Usersdata.objects.filter(email=email)
		if check.exists() == True:
			max_attempts_check = check.values('attempts','attempts_datetime')
			if max_attempts_check[0]['attempts'] == 3:
				now_aware = timezone.now()

				time_check = now_aware-max_attempts_check[0]['attempts_datetime']
				differecn = str(time_check).split(':')[1]
				if differecn >5:
					Usersdata.objects.filter(email=email).update(attempts=None,attempts_datetime=None)
				else:
					data={'message':"Please try after 5 min."}	
					return render(request, "login/login.html",data)
			check_pas = check.filter(password=password)
			if check_pas.exists() == False:
				get_attempts =  check.values('attempts','attempts_datetime')
				if get_attempts[0]['attempts'] == None:
					data={'message':"Please enter valid credentials."}
					Usersdata.objects.filter(email=email).update(attempts=1,attempts_datetime=datetime.now())
				elif get_attempts[0]['attempts'] == 3:
					data={'message':"Please try after 5 min."}	
				else:
					data={'message':"Please enter valid credentials."}
					reporter = Usersdata.objects.get(email=email)
					reporter.attempts = F('attempts') + 1
					reporter.save()
				return render(request, "login/login.html",data)

		check = Usersdata.objects.filter(email=email,password=password)
		if check.exists() == True:
			user_info = check.values()[0]
			request.session['email'] = user_info['email']
			request.session['user_name'] =user_info['user_name']
			if not request.session.session_key:
				request.session.create()
			sessionkey = request.session.session_key
			check_seesion = Userssession.objects.filter(user_id = user_info['id'])
			if check_seesion.exists() == True:
				check_seesion.update(sessionkey=sessionkey)
			else:
				Userssession.objects.create(sessionkey=sessionkey,user_id = user_info['id'])
			Usersdata.objects.filter(email=email).update(attempts=None,attempts_datetime=None)
			return HttpResponseRedirect("/user/profile/")
		else:
			data={'message':"Please enter valid credentials."}
			return render(request, "login/login.html",data)
	else:
		data = {}
		return render(request, "login/login.html",data)
