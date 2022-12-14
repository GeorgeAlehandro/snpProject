from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import urllib.parse
from .models import DiseaseTrait, SNPToDiseaseToReference, SNP, Genes, Reference
from django_datatables_view.base_datatable_view import BaseDatatableView
import natsort
import plotly.graph_objs as go
import pandas as pd
import crispy_forms
import table

def homepage(request):
    return render(request, "homepage.html")

def snppage(request):
    snps = SNP.objects.all()
    chrs = SNP.objects.order_by().values('chrom').distinct()
    return render(request, 'snp_search_page.html', {'snps': snps, 'chrs': chrs})

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
    return render(request, "serverside_diseases_fetch.html")

class SNPToDiseaseToReferenceListView(BaseDatatableView):
    model = SNPToDiseaseToReference

    columns = ['rsid', "strongest_snp", 'diseaseID', 'pubmedid', 'pvalue', 'pvalueMLog', 'ReportedGenes', "ci"]
    def filter_queryset(self, qs):
        disease_filter = self.request.GET.get('diseaseID', None)
        rsid_filter = self.request.GET.get('rsid', None)
        genes_filter = self.request.GET.get('ReportedGenes', None)

        if disease_filter:
            qs = qs.filter(diseaseID__name__iexact=disease_filter)
            list_region = []
            list_pvalueMLog = []
            list_rsidname = []
            list_detail_region = []
            list_links = []
            #Plot figure
            for query in qs:
                list_region.append(query.rsid.chrom)
                list_rsidname.append(query.rsid.rsid)
                list_links.append(
                    "<a href=\"http://127.0.0.1:8000/snpsearch/?snp_id=" + query.rsid.rsid + "&chr=\">+</a>")

                list_pvalueMLog.append(query.pvalueMLog)
                list_detail_region.append(query.rsid.chrom_region)
            # Creating the Figure instance
            df = pd.DataFrame({'chr_region': list_region,
                               'pvalueMLog': list_pvalueMLog,
                               'rsidname': list_rsidname,
                               'detail_region': list_detail_region,
                               'test': list_links})
            df.pvalueMLog = df.pvalueMLog.astype(float)
            df = df.sort_values("chr_region", key=natsort.natsort_keygen())
            plotAnnotes = []
            print(list_links)
            data = [go.Scatter(
                x=df['chr_region'],
                y=df['pvalueMLog'],
                text=df['test'],
                mode='markers+text',
                hovertext="rsid: " + df["rsidname"] + "\n" + "Region:" + df['detail_region'],
                hoverinfo="text"
            )]

            fig = go.Figure(data=data)
            fig.update_layout(title="Distribution of the SNPs related to this trait.", title_x=0.5)
            fig.update_yaxes(title="-Log (PVal)")
            fig.update_xaxes(title="Location of the SNPs", tickmode='linear')
            fig.write_json("/home/ubuntu/snpProject/snpProject/snpProjectDB/static/plot/plot.json")
        if genes_filter:
            qs = qs.filter(ReportedGenes__name__iexact=genes_filter)
        if rsid_filter:
            qs = qs.filter(rsid__rsid__iexact=rsid_filter)
            list_rsidname = []
            list_disease = []
            #Plot figure
            for query in qs:
                list_disease.append(query.diseaseID.name)
            disease_dict = {}
            for disease in list_disease:
                disease_dict[disease] = disease_dict.get(disease, 0) + 1
            fig = go.Figure(data=[go.Pie(labels=list(disease_dict.keys()), values=list(disease_dict.values()), textinfo='label+percent',
                                         insidetextorientation='radial'
                                         )])
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
        elif column == 'rsid':
            link = "/snpsearch/?snp_id=" + str(row.rsid)
            rsid_link = '<a href="%s">'%link +str(row.rsid)+'</a>'
            return rsid_link
        elif column == 'diseaseID':
            link = "/disease/?diseaseID=" + str(row.diseaseID)
            rsid_link = '<a href="%s">'%link +str(row.diseaseID)+'</a>'
            return rsid_link
        return super(SNPToDiseaseToReferenceListView, self).render_column(row, column)



def show_snps(request):
    return render(request, "serverside_snps_fetch.html")

class SNPListView(BaseDatatableView):
    model = SNP
    columns = ['rsid', 'snp_id_current', 'chrom','chrom_pos', 'chrom_region']
    def filter_queryset(self, qs):
        snp_filter = self.request.GET.get('snp_id', None)
        chr_filter = self.request.GET.get('chr', None)
        start_filter = self.request.GET.get('begin_pos', None)
        end_filter = self.request.GET.get('end_pos', None)
        if snp_filter:
            qs = qs.filter(rsid__iexact=snp_filter)
        if chr_filter:
            qs = qs.filter(chrom=chr_filter)
        if start_filter:
            qs = qs.exclude(chrom_pos__exact='')
            qs = qs.filter(chrom_pos__gte=start_filter)
        if end_filter:
            qs = qs.exclude(chrom_pos__exact='')
            qs = qs.filter(chrom_pos__lte=end_filter)
        return qs
    def render_column(self, row, column):
        info = ""
        if column == 'rsid':
            link = "/disease/?rsid=" + str(row.rsid)
            pubmed_link = '<a href="%s">'%link +str(row.rsid)+'</a>'
            return pubmed_link
        return super(SNPListView, self).render_column(row, column)

#"<? echo(urlencode("Replace the spaces here")); ?>"
def show_snp_result(request):
    return render(request, "serverside_snps_fetch.html")

def genespage(request):
    genes = Genes.objects.all()
    return render(request, 'genes_search_page.html', {'genes': genes})

def diseasespage(request):
    diseases = DiseaseTrait.objects.all()
    print(diseases)
    return render(request, 'diseases_search_page.html', {'diseases': diseases})
def show_snptodiseasetoref_result(request):
    return render(request, "serverside_snpstoreferencetodisease_fetch.html")

def show_genes_snptodiseasetoref_result(request):
    return render(request, "serverside_genes_snpstoreferencetodisease_fetch.html")

def docs_mainpage(request):
    return render(request, "docs.html")

def docs_faqpage(request):
    return render(request, "docs_faq.html")
def docs_methodspage(request):
    return render(request, "docs_methods.html")
def docs_userpage(request):
    return render(request, "docs_user.html")

class ReferencesListView(BaseDatatableView):
    model = Reference
    columns = ['pubmedid', 'journal', 'date','title', 'URL']
    def render_column(self, row, column):
        if column == 'pubmedid':
            link = "https://pubmed.ncbi.nlm.nih.gov/" + str(row.pubmedid)
            pubmed_link = '<a href="%s">'%link +str(row.pubmedid)+'</a>'
            return pubmed_link
        elif (column == 'URL'):
            link = "https://"+str(row.URL)
            URL_link = '<a href="%s">'%link +str(row.URL)+'</a>'
            return URL_link
        return super(ReferencesListView, self).render_column(row, column)

def show_references_result(request):
    return render(request, "serverside_references_fetch.html")

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        if (myfile.name.endswith(".txt") or myfile.name.endswith(".tsv")):
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'submit_data.html', {
                'uploaded_file_url': uploaded_file_url
            })
        fail = "failure"
        return render(request, 'submit_data.html', {
            'fail': fail
        })
    return render(request, 'submit_data.html')