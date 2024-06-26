from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# create your views here.
def home (request):
	return render(request,"main/home.html")