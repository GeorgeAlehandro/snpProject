from django.db import models

class SNP(models.Model):
    rsid = models.CharField(max_length=30, primary_key=True) #SNPs ID
    snp_id_current = models.IntegerField(blank=True, null = True)
    chrom = models.CharField(max_length=2)
    chrom_pos = models.IntegerField(blank=True, null = True)
    chrom_region = models.CharField(max_length=30)

    def __str__(self):
        return str(self.rsid)


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
        return str(self.pubmedid)
class Genes(models.Model):
    name = models.CharField(primary_key=True, max_length = 50)

    def __str__(self):
        return self.name
class SNPToDiseaseToReference(models.Model):
 #   id = models.AutoField(models.BigAutoField(primary_key=True))
    rsid = models.ForeignKey(SNP, on_delete=models.CASCADE, default=1)
    diseaseID = models.ForeignKey(DiseaseTrait, on_delete=models.CASCADE,default=1)
    pubmedid = models.ForeignKey(Reference, on_delete=models.CASCADE,default=1)
    pvalue = models.CharField(max_length=200)
    pvalueMLog = models.CharField(max_length=200) #Should be calculated
    ReportedGenes = models.ManyToManyField(Genes)
    def __str__(self):
        return str(self.rsid) + ' ' + str(self.diseaseID) +' ' + str(self.pubmedid)
    #class Meta:
     #   constraints = [
    #        models.UniqueConstraint(
   #             fields = ['rsid', 'diseaseID', 'pubmedid'], name = 'unique_migration_host_combination'
  #          )
 #       ]

