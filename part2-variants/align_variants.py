# Align the PETase variant sequences using MUSCLE
import subprocess
from Bio import SeqIO
import os

# __file__ is the full path to this script (e.g. .../part2-variants/align_variants.py)
# os.path.dirname() strips off the filename, leaving just the folder path
# This means script_dir always points to part2-variants, no matter which
# folder you were standing in when you ran the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output file paths
input_file = os.path.join(script_dir, "data", "petase_variants.fasta")
output_file = os.path.join(script_dir, "data", "aligned_variants.fasta")
muscle_exe = os.path.join(script_dir, "..", "muscle-win64.v5.3.exe")

# Run MUSCLE to align the sequences
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

# Show each variant name and first 60 amino acids of its aligned sequence
print("\nFirst 60 positions of alignment:")
for record in alignment:
    print(f"{record.id[:40]:<40} {str(record.seq[:60])}")
    