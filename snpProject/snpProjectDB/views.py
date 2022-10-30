import natsort
from django.shortcuts import render
from .snpforms import FormSNP
from .tables import SNPtable, SNPToDiseaseToReferencetable
#from helloworldapp.models import Person
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Q
import urllib.parse
from .models import DiseaseTrait, SNPToDiseaseToReference, SNP, Genes
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.http import JsonResponse
from django.utils.encoding import iri_to_uri
import natsort
import plotly.graph_objs as go
import pandas as pd
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
        list_region = []
        list_pvalueMLog = []
        if disease_filter:
            qs = qs.filter(diseaseID__name__iexact=disease_filter)
        genes_filter = self.request.GET.get('ReportedGenes', None)
        if genes_filter:
            qs = qs.filter(ReportedGenes__name__iexact=genes_filter)
        for query in qs:
            list_region.append(query.rsid.chrom)
            list_pvalueMLog.append(query.pvalueMLog)
        # Creating the Figure instance
        print("@@@@@@@")
        df = pd.DataFrame({'chr_region': list_region,
                           'pvalueMLog': list_pvalueMLog})
        df.pvalueMLog = df.pvalueMLog.astype(float)
        df = df.sort_values("chr_region", key = natsort.natsort_keygen())
        print(df)
        data = [go.Scatter(
            x=df['chr_region'],
            y=df['pvalueMLog'],
            mode='markers',


        )]
        fig = go.Figure(data=data)
        fig.update_layout(title="Distribution of the SNPs related to this trait.", title_x=0.5)
        fig.update_yaxes(title="-Log (PVal)")
        fig.update_xaxes(title="Location of the SNPs", tickmode='linear')
        fig.write_json("/home/ubuntu/snpProject/snpProject/snpProjectDB/static/plot/plot.json")
        return qs
    def render_column(self, row, column):
        info = ""
        if column == 'pubmedid':
            link = "https://pubmed.ncbi.nlm.nih.gov/" + str(row.pubmedid)
            pubmed_link = '<a href="%s">'%link +str(row.pubmedid)+'</a>'
            return pubmed_link
        elif (column == 'ReportedGenes'):
            for gene in row.ReportedGenes.all():
                gene_query = "https://www.genecards.org/cgi-bin/carddisp.pl?gene=" + str(gene.name)
                info += '<a href="%s">'%gene_query +gene.name +", " '</a>'
            info = info[:-6]
            return info
        return super(SNPToDiseaseToReferenceListView, self).render_column(row, column)



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
    columns = ['rsid', 'snp_id_current', 'chrom','chrom_pos', 'chrom_region']
    def filter_queryset(self, qs):
        snp_filter = self.request.GET.get('snp_id', None)
        chr_filter = self.request.GET.get('chr', None)
        if snp_filter:
            qs = qs.filter(rsid__istartswith=snp_filter)
        if chr_filter:
            qs = qs.filter(chrom=chr_filter)
        return qs

#"<? echo(urlencode("Replace the spaces here")); ?>"
def show_snp_result(request):
    return render(request, "serverside_snps_fetch.html")

def genespage(request):
    genes = Genes.objects.all()
    return render(request, 'genes_search_page.html', {'genes': genes})
def show_snptodiseasetoref_result(request):
    return render(request, "serverside_snpstoreferencetodisease_fetch.html")

def show_genes_snptodiseasetoref_result(request):
    return render(request, "serverside_genes_snpstoreferencetodisease_fetch.html")