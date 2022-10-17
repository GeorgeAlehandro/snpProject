from snpProjectDB.models import DiseaseTrait, Reference, SNP, SNPToDiseaseToReference, Genes
import copy
import re
f = open('/home/ubuntu/snpProject/trying_to_filter.tsv', "r")
#This is the header
header = f.readline()
header_split = header.split('\t')
indexes_Reference_table = []
columns_Reference_table = ['PUBMEDID', 'JOURNAL', 'DATE', 'STUDY', 'LINK']
for column in columns_Reference_table:
    indexes_Reference_table.append(header_split.index(column))
indexes_DiseaseTrait_table = []
columns_DiseaseTrait_table = ['DISEASE/TRAIT']
for column in columns_DiseaseTrait_table:
    indexes_DiseaseTrait_table.append(header_split.index(column))
print(indexes_DiseaseTrait_table)
indexes_Genes_table = []
columns_Genes_table = ['MAPPED_GENE']
for column in columns_Genes_table:
    indexes_Genes_table.append(header_split.index(column))
indexes_SNP_table = []
columns_SNP_table = ['SNPS', 'SNP_ID_CURRENT', 'CHR_ID', 'CHR_POS', 'REGION']
for column in columns_SNP_table:
    indexes_SNP_table.append(header_split.index(column))
print(header_split)

indexes_SNPToDiseaseToReference_table = []
columns_SNPToDiseaseToReference_table = ['SNPS', 'DISEASE/TRAIT', 'PUBMEDID', 'P-VALUE', 'PVALUE_MLOG', 'REPORTED GENE(S)']
for column in columns_SNPToDiseaseToReference_table:
    indexes_SNPToDiseaseToReference_table.append(header_split.index(column))
print(indexes_SNPToDiseaseToReference_table)

# print(indexes_Reference_table)
i = 0
next_line = f.readline()

while next_line:
    print(i)
    next_line_split = next_line.split('\t')
    for index in indexes_DiseaseTrait_table:
        q = DiseaseTrait(next_line_split[index])
        q.save()
    reference_to_add = [next_line_split[i] for i in indexes_Reference_table]
    ref_to_add = Reference(reference_to_add[0],reference_to_add[1],reference_to_add[2],reference_to_add[3],reference_to_add[4])
    ref_to_add.save()
    SNP_to_add = [next_line_split[i] for i in indexes_SNP_table]
    print(SNP_to_add)
    if (';' in SNP_to_add[0]):
        for a in range(len(SNP_to_add[0].split(';'))):
            new_divided_SNP_to_add = copy.deepcopy(SNP_to_add)
            mew_divided_genes_to_Add = copy.deepcopy(gene)
            new_divided_SNP_to_add[0] = SNP_to_add[0].split(';')[a]
            new_divided_SNP_to_add[2] = SNP_to_add[2].split(';')[a]
            new_divided_SNP_to_add[3] = SNP_to_add[3].split(';')[a]
            print(new_divided_SNP_to_add)
            if type(new_divided_SNP_to_add[1]) != int or float :
                new_divided_SNP_to_add[1] = None

            if type(new_divided_SNP_to_add[3]) != int or float :
                new_divided_SNP_to_add[3] = None
            new_divided_SNP_to_add = SNP(new_divided_SNP_to_add[0], new_divided_SNP_to_add[1], new_divided_SNP_to_add[2], new_divided_SNP_to_add[3],
                                   new_divided_SNP_to_add[4])
            new_divided_SNP_to_add.save()
            SNPtoDisToRef_to_add = [next_line_split[i] for i in indexes_SNPToDiseaseToReference_table]
            ter = SNPToDiseaseToReference(rsid=new_divided_SNP_to_add, diseaseID=q, pubmedid=ref_to_add, pvalue=SNPtoDisToRef_to_add[3],
                                          pvalueMLog=SNPtoDisToRef_to_add[4])
            ter.save()
            Gene_to_add = [next_line_split[i] for i in indexes_Genes_table]
            print(i)
            splitting = re.split(', | - ', Gene_to_add[0])
            for gene in splitting:
                new_divided_genes_to_add = gene.split(';')[a]
                print(new_divided_genes_to_add)
                gene = Genes(name=new_divided_genes_to_add)
                gene.save()
            ter.ReportedGenes.set(splitting)
            i += 1
            next_line = f.readline()
            continue
    if type(SNP_to_add[1]) != int or float :
        SNP_to_add[1] = None

    if type(SNP_to_add[3]) != int or float :
        SNP_to_add[3] = None
    SNP_to_add = SNP(SNP_to_add[0], SNP_to_add[1], SNP_to_add[2], SNP_to_add[3],
                           SNP_to_add[4])
    SNP_to_add.save()
    SNPtoDisToRef_to_add = [next_line_split[i] for i in indexes_SNPToDiseaseToReference_table]
    ter = SNPToDiseaseToReference(rsid=SNP_to_add, diseaseID=q, pubmedid=ref_to_add, pvalue=SNPtoDisToRef_to_add[3],
                                  pvalueMLog=SNPtoDisToRef_to_add[4])
    ter.save()
    Gene_to_add = [next_line_split[i] for i in indexes_Genes_table]
    print(i)
    splitting = re.split(', | - ', Gene_to_add[0])
    for gene in splitting:
        gene = Genes(name=gene)
        gene.save()
    ter.ReportedGenes.set(splitting)


    i+=1
    next_line = f.readline()

print('done')
