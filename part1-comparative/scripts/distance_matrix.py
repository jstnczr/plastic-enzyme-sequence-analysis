# Import tools needed for distance matrix calculation
from Bio import SeqIO
from Bio.Align import substitution_matrices
import numpy as np

# Load the aligned sequences
alignment = list(SeqIO.parse("data/aligned_enzymes.fasta", "fasta"))

# Get enzyme names for labeling
names = [record.id for record in alignment]

# Calculate pairwise identity between all enzyme pairs
print("Calculating pairwise sequence identity...\n")

# Create an empty matrix to fill in
num_seqs = len(alignment)
matrix = [[0.0] * num_seqs for _ in range(num_seqs)]

for i in range(num_seqs):
    for j in range(num_seqs):
        seq1 = str(alignment[i].seq)
        seq2 = str(alignment[j].seq)
        
        # Count positions where both sequences have the same amino acid
        matches = sum(a == b and a != "-" for a, b in zip(seq1, seq2))
        
        # Count total positions that aren't gaps in both sequences
        total = sum(a != "-" or b != "-" for a, b in zip(seq1, seq2))
        
        # Calculate percentage identity
        matrix[i][j] = round((matches / total) * 100, 1)

# Print the distance matrix
print(f"{'':35}", end="")
for name in names:
    print(f"{name[:10]:>12}", end="")
print()

for i, name in enumerate(names):
    print(f"{name[:35]:<35}", end="")
    for j in range(num_seqs):
        print(f"{matrix[i][j]:>12.1f}", end="")
    print()

print("\nValues represent percentage sequence identity (%)")
