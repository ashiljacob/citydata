from django.shortcuts import render
import requests
# Create your views here.
def home(request):
	return render(request,'index.html')

def uae(request):


	
	cities=['Umm al Qaywayn','Ras al-Khaimah','Khawr Fakkān',
		'Dubai','Dibba Al-Fujairah','Dibba Al-Hisn','Sharjah','Ar Ruways','Al Fujayrah',
		'Al Ain','Ajman','Adh Dhayd','Abu Dhabi']
	return render(request,'data.html',{'cities':cities})

def india(request):
	cities = ['Mumbai','Bengaluru','New Delhi','Hyderabad','Chennai','Kochi','Thiruvanathapuram','Ahmedabad',
			'Pune','Bhopal','Lucknow','Gurugram','Kolkata','Kozhikode','Mysuru','Mangalapuram','Coimbatore',
			'Surat','Vadodara','Vizag','Madgaon']
	return render(request,'data.html',{'cities':cities})
def germany(request):
	cities = ['Berlin','Munich','Dusseldorf','Honover','Bavaria','Hamburg','Cologne','Frankfurt']
	return render(request,'data.html',{'cities':cities})

def sweden(request):
	cities=['Alingsås','Åmål','Ängelholm','Arboga','Arvika','Askersund','Avesta','Boden','Bollnäs','Borgholm',
			'Borlänge','Borås','Djursholm','Eksjö','Enköping','Eskilstuna','Eslöv','Fagersta','Falkenberg',
			'Falköping','Falsterbo','Falun','Filipstad','Flen','Gothenburg']
	return render(request,'data.html',{'cities':cities})

	
def austria(request):
	cities = ['Wolfsberg','Wiener Neustadt','Vienna','Wels','Weinzierl bei Krems','Villach','Traun','Traiskirchen'
			,'Ternitz','Steyr','Spittal an der Drau','Schwechat','Sankt Pölten','Salzburg','Saalfelden am Steinernen Meer','Mödling','Lustenau','Linz','Leonding','Leoben','Kufstein','Krems an der Donau','Klosterneuburg'
			,'Klagenfurt am Wörthersee','Kapfenberg','Innsbruck','Hallein','Graz','Feldkirch','Dornbirn','Bregenz','Braunau am Inn'
			,'Baden','Amstetten','Ansfelden']
	return render(request,'data.html',{'cities':cities})

	