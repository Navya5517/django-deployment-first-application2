from django.shortcuts import render;
from django.http import HttpResponse;
import math;

#Create your views here...
def fact(request): 
	return HttpResponse("<h2>math.factorial(8)</h2><hr/>");