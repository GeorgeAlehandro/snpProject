from django.shortcuts import render
#from helloworldapp.models import Person
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
#from .forms import FormPerson
from .models import DiseaseTrait, SNPToDiseaseToReference
from django_serverside_datatable.views import ServerSideDatatableView
from django.http import JsonResponse
def homepage(request):
    return render(request, "homepage.html")

def snppage(request):
    return render(request, "snppage.html")

def all_diseases(request):
    diseases_list = DiseaseTrait.objects.all()
    return render(request, "diseases.html", {'diseases_list': diseases_list})

class DiseasesListView(ServerSideDatatableView):
    queryset = DiseaseTrait.objects.all()
    columns = ['name']

def show_diseases(request):
    return render(request, "serverside_diseases_fetch.html")

class SNPsListView(ServerSideDatatableView):
    queryset = SNPToDiseaseToReference.objects.all()
    columns = ['rsid', 'diseaseID', 'pubmedid', 'pvalue', 'pvalueMLog', 'ReportedGenes']

def show_snps(request):
    return render(request, "serverside_snps_fetch.html")