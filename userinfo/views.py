from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect


# Create your views here.


def registration(request):
	# path = request.get_full_path()
	if request.method == 'POST':
		user_name= (request.POST.get('user_name')).strip()
		last_name= (request.POST.get('last_name')).strip()
		email= (request.POST.get('email')).strip()
		password = hashlib.md5((request.POST.get('password')).strip()).hexdigest()

		print user_name
		print last_name
		print email
		print password
		# print 'email',email
		# print 'password',password
		# print qqq
		# check = Vendors_data.objects.filter(email=email,password=password)
		# if check.exists() == True:
		# 	if int(check.values('status')[0]['status']) == 1 :
		# 		pass
		# 		# vendors_details = check.values()
		# 		# request.session['vendor_email']= email
		# 		# request.session['user_type']= 'vendor'
		# 		# request.session['name']= vendors_details[0]['name']
		# 		# print "vendors_details",vendors_details
		# 		# data=roles.objects.filter(id=vendors_details[0]['role_id']).values()
		# 		# data=eval(data[0]['access_rights'])
		# 		# finaldata=[]
		# 		# for i in data:
		# 		# 	if 'id' in i and 'parent_module_id' in i:
		# 		# 		finaldata.append(i)
		# 		# keyValList=['0']
		# 		# expectedResult = [d for d in finaldata if d['parent_module_id'] in keyValList]
		# 		# if len(expectedResult)>0:
		# 		# 	final_list=self.recursive(expectedResult,finaldata)
		# 		# request.session['side_menu_data']=final_list
		# 		# request.session['role_info']=data
		# 		# sessionkey=request.session.session_key
		# 		# print check.values()
		# 		# print 'sessionkey',sessionkey
		# 		# check.update(key = sessionkey)
		# 		# # print qq
		# 		# return HttpResponseRedirect("/", {"full_name" : vendors_details[0]['name']})
		# 	else:
		# 		data={'message':"Vendor access deactivated."}
		# 		return render(request, "login/login.html",data)
		# else:
		# 	data={'message':"Please enter valid credentials."}
		# 	return render(request, "login/login.html",data)
	else:
		data = {}
		return render(request, "userinfo/registration.html",data)
