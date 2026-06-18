# Comparative Sequence Analysis of Plastic-Degrading Enzymes

**Author:** Justin Temporada  
**Institution:** University of Waterloo, Honours Biology (Bioinformatics Option)  
**Summer 2026**

---

## Background

Plastic waste is a major environmental problem, and one of the more interesting 
biological solutions involves bacteria that have evolved enzymes capable of 
breaking down plastics like PET. This project was directly inspired by Dadzie (2022), 
an MSc thesis proposal from the University of Waterloo on engineering *Pseudomonas 
putida* KT2440 to convert plastic waste into PHA, a biodegradable bioplastic. The 
thesis worked with four plastic-degrading genes — I wanted to understand those 
same enzymes computationally: how related are they, and what do they share at 
the sequence level?

---

## Enzymes

| Enzyme | Organism | Target | NCBI Accession |
|--------|----------|--------|----------------|
| PETase | *Ideonella sakaiensis* | PET | GAP38373.1 |
| MHETase | *Ideonella sakaiensis* | PET intermediate | GAP38911.1 |
| Cut1 (Cutinase) | *Thermobifida fusca* | PET | ADV92528.1 |
| Tcur1278 (Lipase) | *Thermonospora curvata* | PET | CDN67545.1 |
| alkB | *Pseudomonas oleovorans* | Polyethylene | CAB51047.1 |

---

## Pipeline

| Step | Script | Description |
|------|--------|-------------|
| 1 | `fetch_sequences.py` | Download sequences from NCBI |
| 2 | `align_sequences.py` | Align with MUSCLE v5.3 |
| 3 | `distance_matrix.py` | Pairwise % identity between all enzymes |
| 4 | `phylo_tree.R` | Neighbor-Joining phylogenetic tree |
| 5 | `conserved_regions.R` | Identify conserved positions across PET hydrolases |
| 6 | `pymol_visualization.pml` | Visualize conserved residues on PETase structure *(in progress)* |

---

## Findings

PETase, Cut1, and Tcur1278 all share around 45-54% sequence identity with each 
other, grouping together on the phylogenetic tree with strong bootstrap support. 
This suggests they share a common evolutionary ancestor — PETase likely evolved 
from a cutinase or lipase-type enzyme that adapted over time to degrade PET 
specifically. MHETase, despite coming from the same organism as PETase, shares 
less than 10% identity with the other PET hydrolases and sits on its own branch 
entirely — it's a structurally different enzyme that just happens to work alongside 
PETase in *I. sakaiensis*. alkB is the most distant of all, consistent with it 
being a completely different class of enzyme targeting polyethylene rather than PET.

Conservation analysis found 109 positions (14.2% of the alignment) that are 
identical across PETase, Cut1, and Tcur1278. Among these are the catalytic triad 
residues Ser, His, and Asp — the three amino acids that actually perform the 
chemistry of breaking PET's ester bonds. These conserved positions are the 
functional core of PET hydrolase activity and would need to be preserved in any 
protein engineering effort.
