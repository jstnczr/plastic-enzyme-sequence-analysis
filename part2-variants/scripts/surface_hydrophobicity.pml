# Surface hydrophobicity of wild-type PETase
# PDB ID: 6EQE - PETase from Ideonella sakaiensis
# PET is hydrophobic, so hydrophobic surface patches are likely where plastic binds

# Load the structure
fetch 6EQE

# Remove water molecules
remove solvent

# Basic display
bg_color white
hide everything

# Show the protein as a surface (the outside shape plastic would contact)
show surface
color white, all

# Color hydrophobic residues to reveal water-repelling patches
select hydrophobic, resn ALA+VAL+LEU+ILE+PHE+MET+TRP+PRO
color orange, hydrophobic

# Show the catalytic triad location for reference
select catalytic_triad, resi 160+206+237
color red, catalytic_triad

# Save image (results is one level up from scripts)
ray 1200, 900
png ../results/surface_hydrophobicity.png