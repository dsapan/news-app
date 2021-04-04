from django.shortcuts import render,redirect
import requests
from .models import SubModel
from newsproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def home(request):
	if request.method == "POST":
		src=request.POST.get('src')
		try:
			a1="https://newsapi.org/v2/top-headlines"
			a2="?sources=" +src
			a3="&apiKey=" + "dcf42dec7d614e778d3dcd8616ab8182"
			wa= a1+a2+a3
			res= requests.get(wa)
			#print(res)
			data= res.json()
			#print(data)

			info=data['articles']
			return render(request,'home.html',{'info':info,'src':src})
		except Exception as e:
			return render(request,'home.html',{'err':'Issue'})
	else:
		return render(request,'home.html')


def subscribe(request):
	if request.method == "POST" and 'subtn':
		em = request.POST.get('em')
		m=SubModel()
		m.em=em
		m.save()
		subject="Welcome to News App"
		msg=" Thank You for subscribing to News App.You will get latest news notification via mail !"
		send_mail(subject,msg,EMAIL_HOST_USER,[em])
		messages.success(request, 'Successfully Sent The Mail !')
		return redirect(home)

			