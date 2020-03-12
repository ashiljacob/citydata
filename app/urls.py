from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('',views.home),
	path("japan/",views.japan),
    path("india/",views.india),
    path("germany/",views.germany),
    path("swden/",views.sweden),
    path("norway/",views.norway),

]