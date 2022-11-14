"""snpProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from snpProjectDB.views import homepage, snppage, genespage, DiseasesListView, show_diseases, show_snps, simple_upload, SNPListView, show_snp_result, SNPToDiseaseToReferenceListView, show_snptodiseasetoref_result,show_genes_snptodiseasetoref_result, diseasespage, docs_mainpage,docs_methodspage, docs_userpage, show_references_result,ReferencesListView, docs_faqpage
from register import views as v
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = "home"),
    path('snpsearch', snppage, name = "snpsearch"),
    path('diseaseslist', show_diseases, name ="diseaseslist"),
    path('diseasedata/', DiseasesListView.as_view()),
    #path('snplist', show_snps, name ="snplist"),
    re_path(r'^fetchsnp/',SNPListView.as_view(), name='order_snp'),
    re_path(r'^fetchsnptodiseasetoref/',SNPToDiseaseToReferenceListView.as_view(), name='order_snptodiseasetoref'),
    re_path(r'snpsearch/', show_snp_result),
    path("register/", v.register, name="register"),
    path("login/", v.login_request, name='login'),
    path("logout/", v.logout_request, name='logout'),
    path('profile/<username>', v.profile, name='profile'),
    re_path(r'disease/', show_snptodiseasetoref_result),
    re_path(r'genes/', show_genes_snptodiseasetoref_result),
    path('genesearch', genespage, name = "genesearch"),
    path('diseasesearch', diseasespage, name = "diseasesearch"),
    path("docs/faq/", docs_faqpage, name='faq'),
    path("docs/", docs_mainpage, name='docs'),
    path("docs/methods/", docs_methodspage, name='methods'),
    path("docs/user/", docs_userpage, name='methods'),
    path("submitdata/", simple_upload, name='submit_data'),
    path('referencesdata/', ReferencesListView.as_view(), name='order_references'),
   path("references/", show_references_result, name='references'),
]
