from django.shortcuts import render
import requests

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


			