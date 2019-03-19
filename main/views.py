from django.shortcuts import render,redirect
from django.contrib import auth,messages

def do_login(request):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		return redirect('dashboard:mahasiswa-list')
	
	context ={
		'title':'Login',			
	}

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			request.session.set_expiry(3600) # set session 5 menit (5x60)
			auth.login(request,user)
			return redirect('dashboard:mahasiswa-list')
		else:
			messages.error(request,"incorrect username or password")

	return render(request,'login.html',context)


def do_logout(request):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		auth.logout(request)
		messages.success(request,'Logout Success')
		return redirect('login')
	else:
		return redirect('login')