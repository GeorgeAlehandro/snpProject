from django.db import models

class SNP(models.Model):
    rsid = models.CharField(max_length=30, primary_key=True) #SNPs ID
    snp_id_current = models.IntegerField()
    chrom = models.CharField(max_length=2)
    chrom_pos = models.IntegerField()
    chrom_region = models.CharField(max_length=30)

    def __str__(self):
        return self.rsid


class DiseaseTrait(models.Model):
    name = models.CharField(primary_key=True, max_length=200)

    def __str__(self):
        return self.name

class Reference(models.Model):
    pubmedid = models.IntegerField(primary_key=True)
    journal = models.CharField(max_length=30)
    date = models.DateField()
    title = models.CharField(max_length=200)
    URL = models.URLField()

    def __str__(self):
        return self.pubmedid

class SNPToDiseaseToReference(models.Model):
    rsid = models.ForeignKey(SNP, on_delete=models.CASCADE)#SNPs ID
    diseaseID = models.ForeignKey(DiseaseTrait, on_delete=models.CASCADE)
    pubmedid = models.ForeignKey(Reference, on_delete=models.CASCADE)
    pvalue = models.IntegerField()
    pvalueMLog = models.IntegerField() #Should be calculated
    ReportedGenes = models.CharField(max_length=200)
    def __str__(self):
        return self.rsid + ' ' + self.diseaseID +' ' + self.pubmedid

