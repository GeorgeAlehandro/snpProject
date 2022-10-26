from django.shortcuts import render
from .snpforms import FormSNP
from .tables import SNPtable, SNPToDiseaseToReferencetable
#from helloworldapp.models import Person
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Q
import urllib.parse
from .models import DiseaseTrait, SNPToDiseaseToReference, SNP
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.http import JsonResponse
from django.utils.encoding import iri_to_uri
def homepage(request):
    return render(request, "homepage.html")

def snppage(request):
    snps = SNP.objects.all()
    chrs = SNP.objects.order_by().values('chrom').distinct()
    return render(request, 'snp_search_page.html', {'snps': snps, 'chrs': chrs})

def all_diseases(request):
    diseases_list = DiseaseTrait.objects.all()
    return render(request, "diseases.html", {'diseases_list': diseases_list})

class DiseasesListView(BaseDatatableView):
    model = DiseaseTrait
    columns = ['name']

    def render_column(self, row, column):
        if column == 'name':
            link = urllib.parse.quote(row.name)
            print(link)
            link = "/disease/?diseaseID=" + link
            #row.name.replace(" ","%20").replace("(", "%28").replace(")","%29")
            ret = '<a href="%s">'%link +row.name+'</a>'
            return ret
        else:
            return super(DiseasesListView, self).render_column(row, column)

def show_diseases(request):
    print("test")
    return render(request, "serverside_diseases_fetch.html")

class SNPToDiseaseToReferenceListView(BaseDatatableView):
    model = SNPToDiseaseToReference
    columns = ['rsid', "strongest_snp", 'diseaseID', 'pubmedid', 'pvalue', 'pvalueMLog', 'ReportedGenes', "ci"]
    def filter_queryset(self, qs):
            disease_filter = self.request.GET.get('diseaseID', None)
            if disease_filter:
                qs = qs.filter(diseaseID__name__iexact=disease_filter)
            return qs

def show_snps(request):
    return render(request, "serverside_snps_fetch.html")

def formsearch(request):
    snps = SNP.objects.all()
    return render(request, 'snp_search_page.html', {'snps': snps})

def snpresult(request, rsid):
    SNPsfound= SNPtable(SNP.objects.filter(Q(rsid__startswith=rsid)| Q(chrom__startswith=rsid)).values())
    return render(request, "experimental_snp.html", {'SNPsfound': SNPsfound})


class SNPListView(BaseDatatableView):
    model = SNP
    columns = ['rsid', 'snip_id_current', 'chrom','chrom_pos', 'chrom_region']
    def filter_queryset(self, qs):
        snp_filter = self.request.GET.get('snp_id', None)
        chr_filter = self.request.GET.get('chr', None)
        if snp_filter:
            qs = qs.filter(rsid__istartswith=snp_filter)
        if chr_filter:
            qs = qs.filter(chrom__istartswith=chr_filter)
        return qs
#"<? echo(urlencode("Replace the spaces here")); ?>"
def show_snp_result(request):
    return render(request, "serverside_snps_fetch.html")

def diseaseResult(request, disease):
    #disease = disease.replace("+", " ")
    #Diseasesfound = SNPToDiseaseToReference.objects.filter(diseaseID__name__iexact=disease)
   # return render(request, "diseases.html", {'diseases_list': Diseasesfound})
    SNPsfound = SNPToDiseaseToReferencetable(SNPToDiseaseToReference.objects.filter(diseaseID__name__iexact=disease))
    return render(request, "experimental_snp.html", {'SNPsfound': SNPsfound})

def show_snptodiseasetoref_result(request):
    return render(request, "serverside_snpstoreferencetodisease_fetch.html")