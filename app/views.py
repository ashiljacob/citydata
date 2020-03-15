from django.shortcuts import render
import requests
import requests, json

# Create your views here.
def home(request):
	return render(request,'index.html')

#getting weather data of every city in each country
def city(c_name):
	
	url ='http://api.openweathermap.org/data/2.5/weather?appid=5bbc09fcb97056fa46a2a3b463262878&q={}'

	weather_data = []

	for c in c_name:
		r = requests.get(url.format(c)).json()
		#print(r)
		try:
			city_weather ={
				
							'city': c,
							'temparature': round(r['main']['temp']-275,2),
							'description':r['weather'][0]['description'],
							'icon':r['weather'][0]['icon']
							}
			weather_data.append(city_weather) 
		except:
			print("Not Found")
	return weather_data
def uae(request):

	cities=['Umm al Qaywayn','Ras al-Khaimah','Khawr Fakkān',
		'Dubai','Dibba Al-Fujairah','Dibba Al-Hisn','Sharjah','Ar Ruways','Al Fujayrah',
		'Al Ain','Ajman','Adh Dhayd','Abu Dhabi']
	
	
	return render(request,'data.html',{'weather_datas':city(c for c in cities)})
	

def india(request):
	cities = ['Mumbai','Bengaluru','New Delhi','Hyderabad','Chennai','Kochi','Thiruvanathapuram','Ahmedabad',
			'Pune','Bhopal','Lucknow','Gurugram','Kolkata','Kozhikode','Mysuru','Mangalapuram','Coimbatore',
			'Surat','Vadodara','Vizag','Madgaon']
	url ='http://api.openweathermap.org/data/2.5/weather?appid=5bbc09fcb97056fa46a2a3b463262878&q={}'

	return render(request,'data.html',{'weather_datas':city(c for c in cities)})
def germany(request):
	cities = ['Berlin','Munich','Dusseldorf','Honover','Bavaria','Hamburg','Cologne','Frankfurt']
	url ='http://api.openweathermap.org/data/2.5/weather?appid=5bbc09fcb97056fa46a2a3b463262878&q={}'

	return render(request,'data.html',{'weather_datas':city(c for c in cities)})

def sweden(request):
	cities=['Alingsås','Åmål','Ängelholm','Arboga','Arvika','Askersund','Avesta','Boden','Bollnäs','Borgholm',
			'Borlänge','Borås','Djursholm','Eksjö','Enköping','Eskilstuna','Eslöv','Fagersta','Falkenberg',
			'Falköping','Falsterbo','Falun','Filipstad','Flen','Gothenburg']
	url ='http://api.openweathermap.org/data/2.5/weather?appid=5bbc09fcb97056fa46a2a3b463262878&q={}'

	return render(request,'data.html',{'weather_datas':city(c for c in cities)})

	
def austria(request):
	cities = ['Wolfsberg','Wiener Neustadt','Vienna','Wels','Weinzierl bei Krems','Villach','Traun','Traiskirchen'
			,'Ternitz','Steyr','Spittal an der Drau','Schwechat','Sankt Pölten','Salzburg','Saalfelden am Steinernen Meer','Mödling','Lustenau','Linz','Leonding','Leoben','Kufstein','Krems an der Donau','Klosterneuburg'
			,'Klagenfurt am Wörthersee','Kapfenberg','Innsbruck','Hallein','Graz','Feldkirch','Dornbirn','Bregenz','Braunau am Inn'
			,'Baden','Amstetten','Ansfelden']
	url ='http://api.openweathermap.org/data/2.5/weather?appid=5bbc09fcb97056fa46a2a3b463262878&q={}'

	return render(request,'data.html',{'weather_datas':city(c for c in cities)})
	