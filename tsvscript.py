f = open('gwas_catalog_v1.0-associations_e96_r2019-09-24_european_nature_genetics_100000.tsv', "r")
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
# i = 0
# while i < 100:
next_line = f.readline()
next_line_split = next_line.split('\t')
print(next_line_split)
for index in indexes_SNP_table:
    print(next_line_split[index])
# for index in indexes_DiseaseTrait_table:
#     print(next_line_split[index])
# for index in indexes_Reference_table:
#     print(next_line_split[index])
# for index in indexes_SNPToDiseaseToReference_table:
#     print(next_line_split[index])
#     i += 1