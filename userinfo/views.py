from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect
# from .model import Usersdata
from userinfo.models import Usersdata

# Create your views here.
from django.contrib.gis.geoip import GeoIP
# from django.contrib.gis.geoip import GeoIP
from datetime import datetime



def registration(request):
	# path = request.get_full_path()
	if request.method == 'POST':
		print ' iam in'
		user_name= (request.POST.get('user_name')).strip()
		last_name= (request.POST.get('last_name')).strip()
		email= (request.POST.get('email')).strip()
		password = hashlib.md5((request.POST.get('password')).strip()).hexdigest()

		data = {'user_name':user_name, 'last_name':last_name, 'email':email}
		# g = GeoIP()
		ip = request.META.get('REMOTE_ADDR', None)
		print ip
		# gi = pygeoip.GeoIP(GEOIP_DATABASE, pygeoip.GEOIP_STANDARD)

		g = GeoIP()
		print 'kkk',ip
		
		if ip != '127.0.0.1':
		    city = g.city(ip)['city']
		else:
			city = 'Hyderabad'

		print user_name
		print last_name
		print email
		print password
		print city

		check = Usersdata.objects.filter(email=email)
		if check.exists() == False:
			Usersdata.objects.create(user_name = user_name,last_name = last_name,email = email,password = password,location = city,created_datetime=datetime.now())
			return HttpResponseRedirect("/")
		else:
			data={'message':"user with same email already exists"}
			return render(request, "login/login.html",data)
	else:
		return render(request, "userinfo/registration.html",{})
