# Generate engineered PETase variant sequences from wild-type
from Bio import SeqIO
from Bio.Seq import Seq, MutableSeq
from Bio.SeqRecord import SeqRecord
import os

# Load the wild-type PETase sequence from Part 1
script_dir = os.path.dirname(os.path.abspath(__file__))
part1_fasta = os.path.join(script_dir, "..", "part1-comparative", "data", "plastic_enzymes.fasta")

sequences = {r.id: r for r in SeqIO.parse(part1_fasta, "fasta")}
wildtype = sequences["PETase_Ideonella_sakaiensis"]

print(f"Wild-type PETase loaded: {len(wildtype.seq)} amino acids")

# Define the mutations for each variant
# Format: (position, original_aa, new_aa)
variants = {
    "ThermoPETase": [
        (121, "S", "E"),
        (186, "D", "H"),
        (280, "R", "A"),
    ],
    "FAST_PETase": [
        (121, "S", "E"),
        (186, "D", "H"),
        (224, "R", "Q"),
        (233, "N", "K"),
        (280, "R", "A"),
    ],
    "DuraPETase": [
        (117, "L", "F"),
        (119, "Q", "Y"),
        (140, "T", "D"),
        (159, "W", "H"),
        (165, "G", "A"),
        (168, "I", "R"),
        (180, "A", "I"),
        (188, "S", "Q"),
        (214, "S", "H"),
        (280, "R", "A"),
    ]
}

# Create output directory
os.makedirs("data", exist_ok=True)
output_file = os.path.join("data", "petase_variants.fasta")

# Start with wild-type as the baseline
all_records = []
wt_record = SeqRecord(wildtype.seq, id="WT_PETase", description="")
all_records.append(wt_record)
print(f"\nWT_PETase: no mutations")

# Apply mutations for each variant
for variant_name, mutations in variants.items():
    mut_seq = MutableSeq(str(wildtype.seq))

    print(f"\n{variant_name}:")
    for pos, expected, new_aa in mutations:
        index = pos - 1
        actual = mut_seq[index]

        if actual != expected:
            print(f"  WARNING: position {pos} expected {expected} but found {actual}")

        mut_seq[index] = new_aa
        print(f"  {expected}{pos}{new_aa}")

    record = SeqRecord(Seq(str(mut_seq)), id=variant_name, description="")
    all_records.append(record)
    print(f"  {len(mutations)} mutations applied")

# Save all four sequences
with open(output_file, "w") as out_handle:
    SeqIO.write(all_records, out_handle, "fasta")

print(f"\nAll sequences saved to {output_file}")
