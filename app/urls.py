from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('',views.home),
	path("uae/",views.uae),
    path("india/",views.india),
    path("germany/",views.germany),
    path("sweden/",views.sweden),
    path("austria/",views.austria),

]