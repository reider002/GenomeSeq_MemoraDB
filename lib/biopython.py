from Bio import Entrez

# Provide your email address
Entrez.email = "reider737@gmail.com"

# Retrieve gene information for the given cancer gene
handle = Entrez.efetch(db="gene", id="ENSG00000134982", retmode="xml")
record = Entrez.read(handle)

# Extract exon information from the gene record
exons = []
for feature in record[0]["GBSeq_feature-table"]:
    if feature["GBFeature_key"] == "CDS":
        for qualifier in feature["GBFeature_quals"]:
            if qualifier["GBQualifier_name"] == "exon":
                exons.append(qualifier["GBQualifier_value"])

print(exons)