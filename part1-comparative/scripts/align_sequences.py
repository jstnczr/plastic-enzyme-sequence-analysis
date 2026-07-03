# Import tools needed to run MUSCLE and handle sequences
import subprocess
from Bio import SeqIO

# Input and output file paths
input_file = "data/plastic_enzymes.fasta"
output_file = "data/aligned_enzymes.fasta"
muscle_exe = "./muscle-win64.v5.3.exe"

# Run MUSCLE to align the sequences
# subprocess.run launches MUSCLE as an external program
# -align is the input file, -output is where the result goes
print("Running MUSCLE alignment...")
subprocess.run([
    muscle_exe,
    "-align", input_file,
    "-output", output_file
])

print(f"Alignment complete! Saved to {output_file}")

# Read and display basic info about the alignment
alignment = list(SeqIO.parse(output_file, "fasta"))
print(f"\nNumber of sequences aligned: {len(alignment)}")
print(f"Alignment length: {len(alignment[0].seq)} positions")

# Show each enzyme name and first 60 amino acids of its aligned sequence
print("\nFirst 60 positions of alignment:")
for record in alignment:
    print(f"{record.id[:40]:<40} {str(record.seq[:60])}")
