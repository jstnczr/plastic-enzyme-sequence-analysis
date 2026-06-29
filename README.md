# Comparative Sequence Analysis of Plastic-Degrading Enzymes

A computational pipeline for comparing the sequences of plastic-degrading enzymes
using multiple sequence alignment, pairwise identity analysis, phylogenetic
reconstruction, and conservation profiling. Built in Python and R.

---

## Enzymes

| Enzyme | Organism | Target | NCBI Accession |
|--------|----------|--------|----------------|
| PETase | *Ideonella sakaiensis* | PET | GAP38373.1 |
| MHETase | *Ideonella sakaiensis* | PET intermediate (MHET) | GAP38911.1 |
| Cut1 (Cutinase) | *Thermobifida fusca* | PET | AAZ54921.1 |
| Tcur1278 (Lipase) | *Thermonospora curvata* | PET | CDN67545.1 |
| alkB | *Pseudomonas oleovorans* | Polyethylene | CAB51047.1 |

---

## Pipeline

| Step | Script | Description |
|------|--------|-------------|
| 1 | `fetch_sequences.py` | Download protein sequences from NCBI |
| 2 | `align_sequences.py` | Multiple sequence alignment with MUSCLE v5.3 |
| 3 | `distance_matrix.py` | Pairwise % identity between all enzymes |
| 4 | `phylo_tree.R` | Neighbor-Joining phylogenetic tree |
| 5 | `conserved_regions.R` | Identify conserved positions across PET hydrolases |
| 6 | `pymol_visualization.pml` | Visualize catalytic triad on PETase crystal structure (PDB: 6EQE) |

---

## How to Reproduce

```bash
pip install biopython
```

Download the appropriate MUSCLE executable for your OS from
https://github.com/rcedgar/muscle/releases and place it in
the project root. This repo includes the Windows 64-bit version.

```bash
python scripts/fetch_sequences.py
python scripts/align_sequences.py
python scripts/distance_matrix.py
```

In RStudio (set working directory to project root first):
```r
source("scripts/phylo_tree.R")
source("scripts/conserved_regions.R")
```

In PyMOL (open the application and run in the command line):
```
@scripts/pymol_visualization.pml
```

---

## Tools
Python 3.13, Biopython, MUSCLE v5.3, R 4.3, ape, ggplot2, PyMOL

---

## Report
A full write-up of the methods, results, and analysis is available in [`report.md`](report.md).