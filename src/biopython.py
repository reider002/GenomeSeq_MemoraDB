from Bio import SeqIO
#from Bio import SeqRecord
#from Bio import SeqFeature
#from Bio import FeatureLocation

#Set up the Ensembl URL
#TODO: impliment adjustable URL parameters - http://rest.ensembl.org/overlap/region/<species>/<region>?feature=exon
ensembl_url = "http://nov2020.archive.ensembl.org/Homo_sapiens/Location/View?db=core;g=ENSG00000134982;r=5:112707498-112846239"

#Retrieve the sequence data from the Ensembl URL
sequence_record = SeqIO.read(ensembl_url, "fasta")
#Extract the exon features from the sequence record
exon_features = [feature for feature in sequence_record.features if feature.type == "exon"]

#Loop through the exon features and extract the relevant information
for exon_feature in exon_features:
    exon_id = exon_feature.qualifiers.get("exon_id")[0]
    exon_start = exon_feature.location.start
    exon_end = exon_feature.location.end
    exon_length = exon_feature.location.end - exon_feature.location.start + 1
    print(f"Exon {exon_id}: start={exon_start}, end={exon_end}, length={exon_length}")
