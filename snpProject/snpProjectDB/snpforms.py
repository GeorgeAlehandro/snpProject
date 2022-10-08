from django import forms

from .models import SNPToDiseaseToReference

# This form model is based on the person model, so that it takes the good input fields

class FormSNP(forms.ModelForm):

    class Meta:
        model = SNPToDiseaseToReference
        fields = ('rsid',)