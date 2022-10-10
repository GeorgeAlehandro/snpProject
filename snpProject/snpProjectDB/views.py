from django.shortcuts import render
from .snpforms import FormSNP

#from helloworldapp.models import Person
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import DiseaseTrait, SNPToDiseaseToReference, SNP
from django_serverside_datatable.views import ServerSideDatatableView
from django.http import JsonResponse

def homepage(request):
    return render(request, "homepage.html")

def snppage(request):
    # if request.method == "POST":
    #     form = FormSNP(request.POST)
    #     if form.is_valid():
    #         formsnp = form.save(commit=False)
    #         return redirect('/formresult/{}/'.format(formsnp.rsid))
    # else:
    #     print("fle")
    #     form = FormSNP()
    # return render(request, 'snppage.html', {'form': form})

    snps = SNP.objects.all()
     #   if request.method == "POST":
    #        return redirect('/formresult/{}/'.format(request.POST.get("rsid","0")))
    print(snps)
    return render(request, 'snppage.html', {'snps': snps})

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
    columns = ['rsid', "strongest_snp", 'diseaseID', 'pubmedid', 'pvalue', 'pvalueMLog', 'ReportedGenes', "ci"]


def show_snps(request):
    return render(request, "serverside_snps_fetch.html")

def formsearch(request):
    snps = SNP.objects.all()
    return render(request, 'snppage.html', {'snps': snps})

def snpresult(request, rsid):
    html = """<html><h1>Search result</h1><body>
    This is the name that was searched: {}</body></html>""".format(rsid)
   # SNPsfound = SNPToDiseaseToReference.objects.filter(rsid__in=SNP.objects.filter(rsid__startswith=rsid)).values
    SNPsfound = SNP.objects.filter(rsid__startswith=rsid).values()
    for snp in SNPsfound:
        print(snp)
        html += "<br>" + str(snp) + "</br>"
    return HttpResponse(html)

def index(request):
    snps = SNP.objects.all()
    return render(request, 'index.html', {'snps': snps})