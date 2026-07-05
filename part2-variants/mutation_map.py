# Build a table of every position where the PETase variants differ from wild-type
from Bio import SeqIO
import os

# script_dir always points to part2-variants, no matter where you run this from
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the aligned sequences from Script 2
input_file = os.path.join(script_dir, "data", "aligned_variants.fasta")
alignment = list(SeqIO.parse(input_file, "fasta"))

# Turn the list of records into a dictionary so we can look up by name
sequences = {r.id: str(r.seq) for r in alignment}

# Wild-type is our reference — every variant gets compared against this
wildtype_seq = sequences["WT_PETase"]

print(f"Wild-type PETase: {len(wildtype_seq)} positions\n")

# Compare each variant to wild-type, position by position
for variant_name, variant_seq in sequences.items():
    if variant_name == "WT_PETase":
        continue

    print(f"{variant_name}:")
    differences = []

    for i in range(len(wildtype_seq)):
        wt_aa = wildtype_seq[i]
        var_aa = variant_seq[i]

        if wt_aa != var_aa:
            position = i + 1
            differences.append((position, wt_aa, var_aa))
            print(f"  Position {position}: {wt_aa} -> {var_aa}")

    print(f"  Total differences from wild-type: {len(differences)}\n")

print("Mutation mapping complete.")