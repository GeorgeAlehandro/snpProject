from django.shortcuts import render
#from helloworldapp.models import Person
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
#from .forms import FormPerson
from django.http import JsonResponse
def homepage(request):
    return render(request, "homepage.html")

def snppage(request):
    return render(request, "snppage.html")
