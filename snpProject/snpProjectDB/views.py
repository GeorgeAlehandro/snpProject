from django.shortcuts import render
from .snpforms import FormSNP
from .tables import SNPtable
#from helloworldapp.models import Person
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Q

from .models import DiseaseTrait, SNPToDiseaseToReference, SNP
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.http import JsonResponse

def homepage(request):
    return render(request, "homepage.html")

def snppage(request):
    snps = SNP.objects.all()
    chrs = SNP.objects.order_by().values('chrom').distinct()
    return render(request, 'snppage.html', {'snps': snps, 'chrs': chrs})

def all_diseases(request):
    diseases_list = DiseaseTrait.objects.all()
    return render(request, "diseases.html", {'diseases_list': diseases_list})

class DiseasesListView(BaseDatatableView):
    model = DiseaseTrait
    columns = ['name']

    def render_column(self, row, column):
        if column == 'name':
            ret = '<a href="%s">'%row.name +row.name+'</a>'
            return ret
        else:
            return super(DiseasesListView, self).render_column(row, column)

def show_diseases(request):
    print("test")
    return render(request, "serverside_diseases_fetch.html")

class SNPsListView(BaseDatatableView):
    queryset = SNPToDiseaseToReference.objects.all()
    columns = ['rsid', "strongest_snp", 'diseaseID', 'pubmedid', 'pvalue', 'pvalueMLog', 'ReportedGenes', "ci"]


def show_snps(request):
    return render(request, "serverside_snps_fetch.html")

def formsearch(request):
    snps = SNP.objects.all()
    return render(request, 'snppage.html', {'snps': snps})

def snpresult(request, rsid):
    SNPsfound= SNPtable(SNP.objects.filter(Q(rsid__startswith=rsid)| Q(chrom__startswith=rsid)).values())
    return render(request, "experimental_snp.html", {'SNPsfound': SNPsfound})