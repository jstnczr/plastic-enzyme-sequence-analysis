# Import tools from Biopython to fetch sequences from NCBI
# Entrez accesses NCBI database, SeqIO parses the sequence data
from Bio import Entrez, SeqIO

# Tell NCBI who you are - required by NCBI
Entrez.email = "jtempora@uwaterloo.ca"

# List of NCBI accession numbers for the sequences we want to fetch
enzymes = {
    "PETase_Ideonella_sakaiensis": "GAP38373.1",
    "MHETase_Ideonella_sakaiensis": "GAP38374.1",
    "Cutinase_Thermobifida_fusca": "AAZ54921.1",
    "Cutinase_Thermonospora_curvata": "ADV92528.1",
    "alkB_Pseudomonas_oleovorans": "CAB51047.1"
}

# Output file path
output_file = "data/plastic_enzymes.fasta"

# Open output file and fetch each sequence from NCBI
with open(output_file, "w") as out_handle:
    for enzyme_name, accession in enzymes.items():
        print(f"Downloading {enzyme_name}...")

        # Fetch the sequence data in FASTA format
        handle = Entrez.efetch(
            db="protein",
            id=accession,
            rettype="fasta",
            retmode="text"
        )

        # Read sequence and rename to know which enzyme it is
        record = SeqIO.read(handle, "fasta")
        record.id = enzyme_name  
        record.description = ""  # Clear the description for cleaner FASTA output
        SeqIO.write(record, out_handle, "fasta")  # Write to output file
        handle.close()

print(f"All sequences downloaded and saved to {output_file}.")
