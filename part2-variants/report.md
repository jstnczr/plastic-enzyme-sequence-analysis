# Structural Analysis of Engineered PETase Variants

**Justin Temporada**
Honours Biology, Bioinformatics Option
University of Waterloo
Summer 2026

---

## Abstract

PETase from *Ideonella sakaiensis* has limited catalytic efficiency and thermal
stability in its wild-type form, which has led to several protein engineering
efforts aimed at improving its performance. This project presents a computational
analysis of three engineered PETase variants: ThermoPETase (3 mutations),
FAST-PETase (5 mutations), and DuraPETase (10 mutations). Variant sequences
were generated programmatically from wild-type PETase by applying the specific
point mutations reported in the literature, with each position verified against
the PDB 6EQE crystal structure numbering. All 18 mutation positions across the
three variants were confirmed to match the expected wild-type residues with zero
mismatches. Structural mapping onto the wild-type PETase structure in PyMOL
revealed that ThermoPETase and DuraPETase mutations cluster near the active site
and core structural regions, while FAST-PETase's two unique mutations (R224Q,
N233K) are positioned further from the catalytic centre. R280A is the only
mutation shared across all three variants. Surface hydrophobicity analysis showed
that hydrophobic patches on the enzyme surface are distributed unevenly, with
concentrations near the active site region where PET binding is expected to occur.

---

## Introduction

Wild-type PETase from *Ideonella sakaiensis* is capable of degrading PET plastic
at moderate temperatures, but its catalytic efficiency and thermal stability are
too low for practical applications (Yoshida et al., 2016). This has motivated
several research groups to engineer improved variants through targeted point
mutations, with the goal of increasing either the enzyme's thermostability, its
catalytic rate, or both.

ThermoPETase was the first major engineered variant, created by Son et al. (2019)
through rational protein engineering. Three mutations (S121E, D186H, R280A) were
introduced to stabilize the region around the active site, resulting in an 8.8
degree increase in melting temperature and a 14-fold improvement in PET
degradation activity at 40 degrees Celsius.

FAST-PETase was developed by Lu et al. (2022) using a machine learning algorithm
called MutCompute to predict beneficial mutations. It was built on the
ThermoPETase scaffold, keeping its three mutations and adding two more (R224Q,
N233K) for a total of five. FAST-PETase is currently one of the most effective
PETase variants for degrading PET at moderate temperatures.

DuraPETase was engineered by Cui et al. (2021) using a computational strategy
called GRAPE (Greedy Accumulated Strategy for Protein Engineering). The process
began with 253 computationally predicted stabilizing mutations, which were
filtered down to 85 candidates and then to 21 experimentally confirmed variants.
These 21 were clustered and combined through greedy accumulation, producing a
final variant with 10 mutations that showed a 31 degree increase in melting
temperature and over 300-fold higher degradation activity compared to wild-type.

This project was motivated by the comparative sequence analysis completed in
Part 1, which established that PETase belongs to the serine hydrolase superfamily
and shares conserved features with related cutinases and lipases. Part 2 narrows
the focus to PETase itself, asking where the engineering mutations are located on
the enzyme structure and whether their positions are consistent with their
reported functional effects.

---

## Methods

### Variant Sequence Generation

Variant sequences were generated programmatically from the wild-type PETase
sequence (NCBI accession GAP38373.1) using a custom Python script. For each
variant, the known point mutations were applied to a copy of the wild-type
sequence. Before each mutation was applied, the script verified that the amino
acid at the target position matched the expected wild-type residue, providing a
check against numbering mismatches between the sequence and the literature.

**Table 1.** Engineered PETase variants analyzed.

| Variant | Mutations | Source |
|---------|-----------|--------|
| ThermoPETase | S121E, D186H, R280A | Son et al. 2019 |
| FAST-PETase | S121E, D186H, R224Q, N233K, R280A | Lu et al. 2022 |
| DuraPETase | L117F, Q119Y, T140D, W159H, G165A, I168R, A180I, S188Q, S214H, R280A | Cui et al. 2021 |

### Sequence Alignment

The four sequences (wild-type plus three variants) were aligned using MUSCLE
v5.3 (Edgar, 2022) to confirm positional correspondence across variants.

### Mutation Mapping

A custom Python script compared each variant to wild-type position by position
across the full alignment, identifying and recording every differing position.

### Structural Visualization

Mutation sites were mapped onto the wild-type PETase crystal structure (PDB:
6EQE) in PyMOL. Mutations were colour-coded by variant: green for ThermoPETase
(positions 121, 186, 280), purple for FAST-PETase's unique additions (positions
224, 233), orange for DuraPETase's unique mutations (positions 117, 119, 140,
159, 165, 168, 180, 188, 214), and yellow for R280A (position 280), the only
mutation shared across all three variants. The catalytic triad (Ser160, Asp206,
His237) was shown in red as a reference for the active site location.

### Surface Hydrophobicity Analysis

The wild-type PETase structure was displayed as a molecular surface in PyMOL,
with hydrophobic residues (Ala, Val, Leu, Ile, Phe, Met, Trp, Pro) coloured
orange against a white background. This provides a simplified view of which
surface regions are water-repelling and therefore more likely to interact with
hydrophobic PET plastic. The catalytic triad was highlighted in red for
reference. This approach classifies residues as hydrophobic or not based on
amino acid identity rather than using a continuous hydrophobicity scale such as
Kyte-Doolittle, which is a limitation worth noting.

---

## Results

### Variant Sequence Verification

All 18 mutation positions across the three variants were applied without any
warnings. The wild-type amino acid at every position matched the expected
residue from the literature, confirming that the sequence numbering is consistent
with the PDB 6EQE structure numbering. ThermoPETase differs from wild-type at
exactly 3 positions, FAST-PETase at 5, and DuraPETase at 10.

### Sequence Alignment

MUSCLE alignment of the four sequences produced an alignment length of 290
positions with no gaps introduced, confirming that the variants differ only by
point substitutions with no insertions or deletions relative to wild-type.

### Mutation Positions

The mutation mapping confirmed every expected position and amino acid change
(Table 2).

**Table 2.** Mutation positions confirmed by computational comparison to wild-type.

| Position | Wild-type | ThermoPETase | FAST-PETase | DuraPETase |
|----------|-----------|-------------|-------------|------------|
| 117 | L | L | L | **F** |
| 119 | Q | Q | Q | **Y** |
| 121 | S | **E** | **E** | S |
| 140 | T | T | T | **D** |
| 159 | W | W | W | **H** |
| 165 | G | G | G | **A** |
| 168 | I | I | I | **R** |
| 180 | A | A | A | **I** |
| 186 | D | **H** | **H** | D |
| 188 | S | S | S | **Q** |
| 214 | S | S | S | **H** |
| 224 | R | R | **Q** | R |
| 233 | N | N | **K** | N |
| 280 | R | **A** | **A** | **A** |

R280A is the only mutation present in all three engineered variants.

### Structural Mapping

Mapping the mutation sites onto the PETase crystal structure (Figure 1) revealed
several patterns. ThermoPETase's mutations (green) and several of DuraPETase's
mutations (orange) are located near the catalytic triad (red), in the region
surrounding the active site. This is consistent with these mutations being
designed to stabilize the protein fold in the vicinity of the catalytic
machinery without disrupting the active site itself.

FAST-PETase's two unique mutations (purple, positions 224 and 233) are
positioned further from the active site, on opposite sides of the protein. These
were identified by the MutCompute algorithm rather than by rational design
focused on the active site region, which may explain their more dispersed
placement.

DuraPETase's nine unique mutations (orange) are spread broadly across the
structure, consistent with a global stability engineering approach rather than
targeted active site optimization. The GRAPE strategy that produced DuraPETase
was designed to reinforce the protein fold at multiple points, and the dispersed
distribution of its mutations reflects this.

R280A (yellow, position 280) sits on the protein surface, away from the active
site. The fact that three independent engineering efforts all identified this
same surface mutation suggests that R280A provides a broadly beneficial effect,
possibly related to surface properties or protein-plastic interaction rather
than catalytic mechanism.

### Surface Hydrophobicity

The surface hydrophobicity map (Figure 2) shows that hydrophobic patches (orange)
are distributed unevenly across the enzyme surface. Several hydrophobic regions
are concentrated near the active site area (red), which is consistent with the
expectation that the enzyme surface near the catalytic centre needs to interact
with hydrophobic PET substrate. The hydrophobic surface patches may represent
the regions where PET plastic initially contacts and binds to the enzyme before
being positioned for hydrolysis.

---

## Discussion

The structural mapping of engineered mutations onto wild-type PETase reveals that
the three engineering strategies took meaningfully different approaches to
improving the same enzyme. ThermoPETase concentrated its three mutations near the
active site to stabilize the local fold, while DuraPETase distributed ten
mutations broadly across the structure to reinforce global stability. FAST-PETase
inherited ThermoPETase's active-site-proximal mutations and added two more at
dispersed positions identified by machine learning. These different strategies
resulted in different types of improvement: ThermoPETase primarily gained
thermostability, DuraPETase gained long-term durability, and FAST-PETase achieved
the highest catalytic rate at moderate temperatures.

The convergence of all three variants on R280A is the most notable finding from
this analysis. Position 280 sits on the protein surface rather than near the
active site, and the mutation from arginine to alanine removes a large, charged
side chain and replaces it with a small, nonpolar one. This surface change may
improve enzyme-plastic interaction by altering the local surface properties in a
way that benefits all three engineering goals simultaneously. The fact that Son
et al. (2019), Lu et al. (2022), and Cui et al. (2021) all independently arrived
at this same mutation, despite using different engineering methods, provides
strong evidence that R280A addresses a fundamental limitation of the wild-type
enzyme.

The surface hydrophobicity analysis provides a simplified but informative view
of how the enzyme's surface properties relate to plastic binding. PET is a
hydrophobic polymer, so the hydrophobic patches visible on the enzyme surface
are the regions most likely to mediate initial contact with the substrate. The
concentration of hydrophobic residues near the active site suggests that the
enzyme's binding surface and catalytic centre are spatially coupled, which is
consistent with a mechanism where the enzyme must grip the plastic surface and
position the ester bond for hydrolysis simultaneously.

A limitation of the hydrophobicity analysis is that it classifies residues
as either hydrophobic or not based on amino acid identity alone, without using
a continuous scale like Kyte-Doolittle. A more quantitative analysis could
provide a finer-grained picture of surface properties, but the binary
classification used here is sufficient to identify the general distribution of
hydrophobic regions and their spatial relationship to the active site.

This analysis builds on the comparative work in Part 1, which established that
PETase belongs to the serine hydrolase superfamily and shares 113 conserved
residues with related cutinases and lipases. The engineering mutations analyzed
here do not fall at any of those conserved positions, which makes biological
sense: conserved residues are the ones evolution has been unable to change
without breaking function, so successful engineering mutations would be expected
to target non-conserved positions where changes can improve performance without
disrupting the core fold or catalytic mechanism.

---

## Conclusion

Structural mapping of ThermoPETase, FAST-PETase, and DuraPETase mutations onto
the wild-type PETase structure reveals that the three engineering approaches
targeted different regions of the protein, consistent with their different
reported improvements in thermostability, catalytic rate, and durability. R280A
is the only mutation shared across all three variants and sits on the protein
surface, suggesting it addresses a fundamental limitation of the wild-type
enzyme. Surface hydrophobicity analysis shows that hydrophobic patches
concentrate near the active site, consistent with the enzyme needing to bind
hydrophobic PET substrate near where hydrolysis occurs. Together, these findings
provide a structural perspective on why specific mutations improve PETase
performance and how future engineering efforts might build on these results.

---

## References

Cui, Y. et al. 2021. Computational redesign of a PETase for plastic
biodegradation under ambient condition by the GRAPE strategy. ACS Catalysis.
11: 1340-1350.

Edgar, R.C. 2022. MUSCLE v5 enables improved estimates of phylogenetic tree
confidence by ensemble bootstrapping. bioRxiv.

Lu, H. et al. 2022. Machine learning-aided engineering of hydrolases for PET
depolymerization. Nature. 604: 662-667.

Son, H.F. et al. 2019. Rational protein engineering of thermo-stable PETase
from Ideonella sakaiensis for highly efficient PET degradation. ACS Catalysis.
9: 3519-3526.

Yoshida, S. et al. 2016. A bacterium that degrades and assimilates poly(ethylene
terephthalate). Science. 351: 1196-1199.