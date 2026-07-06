# Comparative Sequence and Structural Analysis of Plastic-Degrading Enzymes

**Justin Temporada**
Honours Biology, Bioinformatics Option
University of Waterloo
Summer 2026

---

## Abstract

Plastic pollution is a growing environmental concern, and microbial enzymes capable
of breaking down synthetic polymers have become an increasingly studied area of
research. This project presents a comparative computational analysis of five
plastic-degrading enzymes: PETase and MHETase from *Ideonella sakaiensis*, Cut1
from *Thermobifida fusca*, Tcur1278 from *Thermonospora curvata*, and alkB from
*Pseudomonas oleovorans*. Protein sequences were retrieved from NCBI, aligned
using MUSCLE v5.3, and analyzed for pairwise sequence identity, phylogenetic
relationships, and sequence conservation. PETase, Cut1, and Tcur1278 share 45-54%
pairwise identity and cluster together in a rooted Neighbor-Joining tree, which
is consistent with shared ancestry within the serine hydrolase superfamily.
Conservation analysis across these three enzymes identified 113 fully conserved
positions out of 775 total alignment positions (14.6%), including the catalytic
triad residues Ser160, Asp206, and His237. Structural visualization in PyMOL using
the PETase crystal structure (PDB: 6EQE) confirmed that these residues are spatially
clustered in the active site. MHETase and alkB showed low sequence identity with
the PET hydrolases, which is consistent with their different structural folds and
biochemical mechanisms.

---

## Introduction

Plastic waste is a major environmental problem, with most plastic produced globally
accumulating in ecosystems rather than being recycled or broken down (Amobonye et
al., 2021). Polyethylene terephthalate (PET) is one of the most widely used
synthetic polymers and is particularly difficult to degrade because of its
hydrophobic surface, high molecular weight, and semi-crystalline structure (Kawai
et al., 2020). Common disposal methods like incineration and landfilling have their
own environmental drawbacks, which has increased interest in biological approaches
to plastic breakdown.

A key development in this area came in 2016 when *Ideonella sakaiensis* 201-F6
was isolated as a bacterium capable of using low-crystallinity PET as a primary
carbon and energy source (Yoshida et al., 2016). This organism produces two
enzymes, PETase and MHETase, that work sequentially to break PET down into its
monomers, terephthalic acid and ethylene glycol. PETase cleaves the ester bonds
of PET to produce mono(2-hydroxyethyl) terephthalate (MHET), and MHETase then
hydrolyzes MHET into the final products.

PETase belongs to the serine hydrolase superfamily, which is defined by an
αβ hydrolase fold and a catalytic triad of serine, histidine, and aspartate
residues (Danso et al., 2019). Other enzymes in this family, including cutinases
from *Thermobifida* and *Thermonospora* species, have also been shown to hydrolyze
PET even though they originally evolved to break down plant polyesters like cutin
(Maurya et al., 2020). This raises a question about where PET-degrading activity
came from: did PETase evolve on its own, or does it share an ancestor with
existing serine hydrolases that happened to have a compatible active site?

This project was directly inspired by Dadzie (2022), an MSc thesis proposal from
the University of Waterloo that examined the same enzyme set in the context of
engineering *Pseudomonas putida* KT2440 to produce polyhydroxyalkanoates (PHA)
from plastic feedstock. The goal here was to take a computational approach to
those same enzymes using a pipeline built in Python and R, to look at their
sequence relationships, identify conserved residues, and confirm the location of
the catalytic triad in the PETase crystal structure.

---

## Methods

### Sequence Retrieval

Protein sequences for five enzymes were downloaded from the NCBI protein database
using Biopython's Entrez interface and saved in FASTA format (Table 1).

**Table 1.** Enzymes analyzed and their NCBI accession numbers.

| Enzyme | Organism | Plastic Target | Accession |
|--------|----------|----------------|-----------|
| PETase | *Ideonella sakaiensis* | PET | GAP38373.1 |
| MHETase | *Ideonella sakaiensis* | PET intermediate | GAP38911.1 |
| Cut1 (Cutinase) | *Thermobifida fusca* | PET | AAZ54921.1 |
| Tcur1278 (Lipase) | *Thermonospora curvata* | PET | CDN67545.1 |
| alkB | *Pseudomonas oleovorans* | Polyethylene | CAB51047.1 |

### Multiple Sequence Alignment

Sequences were aligned using MUSCLE v5.3 (Edgar, 2022), run as an external
subprocess through Python. The resulting alignment was used as input for all
downstream analyses.

### Pairwise Identity Analysis

Pairwise percentage sequence identity was calculated from the alignment using a
custom Python script. For each pair of sequences, identity was calculated as the
number of positions with matching amino acids divided by the total number of
positions, excluding columns where both sequences had gaps.

### Phylogenetic Analysis

A Neighbor-Joining (NJ) phylogenetic tree was constructed in R using the ape
package (Paradis and Schliep, 2019). Amino acid distances were calculated using
dist.aa() and the tree was rooted using alkB as the outgroup, since it belongs
to a different enzyme class from all other sequences in the dataset. Bootstrap
support was assessed with 1000 replicates.

### Conservation Analysis

Conserved positions were identified across PETase, Cut1, and Tcur1278, which are
the three PET serine hydrolases in the dataset. A position was considered fully
conserved if all three sequences had the same amino acid with no gaps at that
position. Conservation scores were calculated as the frequency of the most common
amino acid at each position and visualized using ggplot2.

### Structural Visualization

The PETase crystal structure (PDB: 6EQE) was loaded in PyMOL and the catalytic
triad residues Ser160, Asp206, and His237 were highlighted to examine their
positions in the active site.

---

## Results

### Pairwise Sequence Identity

PETase shares 47.4% identity with Cut1 and 45.3% with Tcur1278, while Cut1 and
Tcur1278 share 53.7% identity with each other. MHETase shares less than 11%
identity with any of the three PET hydrolases despite coming from the same
organism as PETase. alkB shares between 4.5% and 12.3% identity with all other
sequences in the dataset (Table 2).

**Table 2.** Pairwise percentage sequence identity (%) across all five enzymes.

|  | PETase | MHETase | Cut1 | Tcur1278 | alkB |
|--|--------|---------|------|----------|------|
| PETase | 100.0 | 9.4 | 47.4 | 45.3 | 10.6 |
| MHETase | 9.4 | 100.0 | 10.1 | 10.8 | 4.5 |
| Cut1 | 47.4 | 10.1 | 100.0 | 53.7 | 12.3 |
| Tcur1278 | 45.3 | 10.8 | 53.7 | 100.0 | 11.4 |
| alkB | 10.6 | 4.5 | 12.3 | 11.4 | 100.0 |

### Phylogenetic Relationships

The rooted Neighbor-Joining tree placed PETase, Cut1, and Tcur1278 together on a
single clade with strong bootstrap support (1000/1000). Cut1 and Tcur1278 are
cutinase and lipase enzymes that naturally target plant polyesters rather than
PET, but they are still the closest relatives of PETase in this dataset. This
suggests that PET-degrading activity in *I. sakaiensis* may have evolved from an
existing serine hydrolase rather than arising on its own. MHETase and alkB both
sit on long isolated branches, which reflects that they belong to different enzyme
classes with different mechanisms (Figure 1).

### Conserved Residues

Conservation analysis across PETase, Cut1, and Tcur1278 identified 113 fully
conserved positions out of 775 total alignment positions, representing 14.6% of
the alignment. These include the catalytic triad residues Ser160, Asp206, and
His237 in PETase numbering, which are identical across all three enzymes. The
conservation profile shows that conserved positions are distributed throughout
the alignment rather than clustered in one region, which is consistent with the
αβ hydrolase fold being maintained across the whole protein structure (Figure 2).

### Structural Confirmation

Visualization of the PETase crystal structure (PDB: 6EQE) in PyMOL showed that
Ser160, Asp206, and His237 are positioned close to each other in the active site.
In the serine hydrolase catalytic mechanism, Ser160 acts as the nucleophile that
attacks the ester bond, His237 acts as a base to activate the serine, and Asp206
stabilizes the histidine through a hydrogen bond (Figure 3).

---

## Discussion

The identity values between PETase, Cut1, and Tcur1278 (45-54%) place them in
the same serine hydrolase family, but the level of divergence suggests they
separated from a common ancestor long before PET was introduced into the
environment. This supports the idea that PETase evolved from a cutinase-like
ancestor that already had the αβ hydrolase fold and the Ser-His-Asp triad needed
for ester bond hydrolysis (Danso et al., 2019; Austin et al., 2018). The fact
that Cut1 and Tcur1278 naturally target plant polyesters rather than PET, yet
are still PETase's closest relatives here, suggests the active site geometry of
these enzymes was already compatible with synthetic polyesters before PET existed
as a substrate.

Finding 113 conserved residues across the three PET hydrolases, including all
three catalytic triad positions, shows that the serine hydrolase fold is highly
constrained at the sequence level. Residues that are identical across three
diverged enzymes are likely either directly involved in catalysis or important
for maintaining protein structure, since mutations there would probably reduce
function and be selected against. The triad residues Ser160, Asp206, and His237
are the most functionally critical of these, and their conservation across
PETase, Cut1, and Tcur1278 supports a shared hydrolytic mechanism.

The isolated phylogenetic positions of MHETase and alkB reflect their different
biochemistry. MHETase belongs to the tannase family and uses a different fold to
hydrolyze the MHET intermediate that PETase produces (Knott et al., 2020). alkB
is a membrane-bound monooxygenase that targets polyethylene through oxidation
rather than hydrolysis, which is a fundamentally different mechanism from ester
bond cleavage (van Beilen et al., 1994). Including both as comparators was useful
because their distance from the PET hydrolases in both sequence and phylogenetic
space helps show how distinct the serine hydrolase cluster actually is.

This project was motivated by Dadzie (2022), which proposed engineering
*Pseudomonas putida* KT2440 to express PET and polyethylene degradation genes
and use the resulting monomers as feedstock for PHA production. The four genes
central to that proposal, PETase, Cut1, Tcur1278, and alkB, are the same enzymes
analyzed here. Knowing which residues are conserved across these enzymes is
relevant to that kind of work, since conserved positions are more likely to be
functionally important and less tolerant of modification.

---

## Conclusion

PETase, Cut1, and Tcur1278 form a related group within the serine hydrolase
superfamily, sharing 113 fully conserved positions including the Ser-His-Asp
catalytic triad responsible for ester bond hydrolysis. The phylogenetic tree
supports the idea that PET-degrading activity evolved from a pre-existing serine
hydrolase rather than arising independently. MHETase and alkB are clearly distinct
from this group in both sequence identity and mechanism. The pipeline developed
here provides a reproducible way to compare plastic-degrading enzymes as more
sequences continue to be discovered and characterized.

---

## References

Amobonye, A., Bhagwat, P., Singh, S., Pillai, S. 2021. Plastic biodegradation:
frontline microbes and their enzymes. Science of the Total Environment. 759: 143536.

Austin, H.P. et al. 2018. Characterization and engineering of a plastic-degrading
aromatic polyesterase. Proceedings of the National Academy of Sciences. 115: E4350-E4357.

Dadzie, E. 2022. Biocatalytic Production of PHA Using Petrochemical Plastics as
Feedstock. MSc Thesis Proposal, University of Waterloo. Supervisor: Dr. Trevor Charles.

Danso, D., Chow, J., Streit, W.R. 2019. Plastics: environmental and biotechnological
perspectives on microbial degradation. Applied and Environmental Microbiology. 85: e01095-19.

Edgar, R.C. 2022. MUSCLE v5 enables improved estimates of phylogenetic tree
confidence by ensemble bootstrapping. bioRxiv.

Kawai, F., Kawabata, T., Oda, M. 2020. Current state and perspectives related to
the polyethylene terephthalate hydrolases available for biorecycling. ACS Sustainable
Chemistry and Engineering. 8: 8894-8908.

Knott, B.C. et al. 2020. Characterization and engineering of a two-enzyme system
for plastics depolymerization. Proceedings of the National Academy of Sciences.
117: 25476-25485.

Maurya, A., Bhattacharya, A., Khare, S.K. 2020. Enzymatic remediation of
polyethylene terephthalate (PET)-based polymers for effective management of plastic
wastes. Frontiers in Bioengineering and Biotechnology. 8: 602325.

Paradis, E., Schliep, K. 2019. ape 5.0: an environment for modern phylogenetics
and evolutionary analyses in R. Bioinformatics. 35: 526-528.

van Beilen, J.B., Wubbolts, M.G., Witholt, B. 1994. Genetics of alkane oxidation
by Pseudomonas oleovorans. Biodegradation. 5: 161-174.

Yoshida, S. et al. 2016. A bacterium that degrades and assimilates poly(ethylene
terephthalate). Science. 351: 1196-1199.