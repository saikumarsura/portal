from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect
from userinfo.models import Usersdata
from django.contrib.gis.geoip import GeoIP
from datetime import datetime



def registration(request):
	if request.method == 'POST':
		user_name= (request.POST.get('user_name')).strip()
		last_name= (request.POST.get('last_name')).strip()
		email= (request.POST.get('email')).strip()
		password = hashlib.md5((request.POST.get('password')).strip()).hexdigest()
		data = {'user_name':user_name, 'last_name':last_name, 'email':email}
		ip = request.META.get('REMOTE_ADDR', None)
		g = GeoIP()
		if ip != '127.0.0.1':
		    city = g.city(ip)['city']
		else:
			city = 'Hyderabad'

		check = Usersdata.objects.filter(email=email)
		if check.exists() == False:
			Usersdata.objects.create(user_name = user_name,last_name = last_name,email = email,password = password,location = city,created_datetime=datetime.now())
			return HttpResponseRedirect("/")
		else:
			data={'message':"user with same email already exists"}
			return render(request, "login/login.html",data)
	else:
		return render(request, "userinfo/registration.html",{})
