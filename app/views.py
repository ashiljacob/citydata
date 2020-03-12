from django.shortcuts import render
import requests
# Create your views here.
def home(request):
	return render(request,'index.html')

def japan(request):


	url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

	querystring = {"lang":"en","lon":"76.267303","lat":"9.931233"}

	headers = {
	    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
	    'x-rapidapi-key': "8b95dc98dfmshe4830a2f6d62476p1e579ejsn4cc940b3bd17"
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)
	
	print(response)
	
	return render(request,'data.html')

def india(request):
	pass
	
def germany(request):
	pass
	
def sweden(request):
	pass
	
def norway(request):
	pass
	