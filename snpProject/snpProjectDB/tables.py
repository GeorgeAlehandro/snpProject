from .models import SNP
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