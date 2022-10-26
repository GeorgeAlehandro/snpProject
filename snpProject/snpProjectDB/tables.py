from .models import SNP, SNPToDiseaseToReference
from table import Table
from table.columns import Column

class SNPtable(Table):
    rsid = Column(field='rsid')
    snp_id_current = Column(field='snp_id_current')
    chrom = Column(field='chrom')
    chrom_pos = Column(field='chrom_pos')
    chrom_region = Column(field='rsichrom_regiond')
    class Meta:
        model = SNP

class SNPToDiseaseToReferencetable(Table):
    rsid = Column(field='rsid')
    strongest_snp = Column(field='strongest_snp')
    diseaseID = Column(field='diseaseID')
    pubmedid = Column(field='pubmedid')
    pvalue = Column(field='pvalue')
    pvalueMLog = Column(field='pvalueMLog')
    ReportedGenes = Column(field='ReportedGenes')
    ci = Column(field='ci')
    class Meta:
        model = SNPToDiseaseToReference