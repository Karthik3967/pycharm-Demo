from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
def home(request):
    #name="Karthik"
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")