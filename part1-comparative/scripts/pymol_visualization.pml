# PyMOL visualization script for PETase structure
# PDB ID: 6EQE - PETase from Ideonella sakaiensis

# Load PETase structure from Protein Data Bank
fetch 6EQE

# Remove water molecules so they don't clutter the image
remove solvent

# Basic display settings
bg_color white
hide everything
show cartoon

# Colour the whole protein grey
color grey80, all

# Highlight the catalytic triad - Ser160, Asp206, His237
# (verified against PDB 6EQE numbering and multiple published sources)
select catalytic_triad, resi 160+206+237
color red, catalytic_triad
show sticks, catalytic_triad

# Save image
ray 1200, 900
png results/petase_structure.png