from django.contrib import admin

from .models import SNP
from .models import DiseaseTrait
from .models import Reference
from .models import SNPToDiseaseToReference
from .models import Genes


admin.site.register(SNP)
admin.site.register(DiseaseTrait)
admin.site.register(Reference)
admin.site.register(SNPToDiseaseToReference)
admin.site.register(Genes)