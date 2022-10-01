from django.contrib import admin

from .models import SNP
from .models import DiseaseTrait
from .models import Reference
from .models import SNPToDiseaseToReference

admin.site.register(SNP)
admin.site.register(DiseaseTrait)
admin.site.register(Reference)
admin.site.register(SNPToDiseaseToReference)
