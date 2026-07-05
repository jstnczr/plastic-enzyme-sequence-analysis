# Load the PETase crystal structure directly from the PDB
fetch 6eqe, async=0

# Remove water molecules so they don't clutter the view
remove solvent

# Show the protein as a cartoon (ribbons showing the fold)
hide everything
show cartoon
color grey80

# Select the three catalytic triad residues
select catalytic_ser, resi 160 and resn SER
select catalytic_asp, resi 206 and resn ASP
select catalytic_his, resi 237 and resn HIS

# Show the triad residues as sticks so their side chains are visible
show sticks, catalytic_ser or catalytic_asp or catalytic_his

# Color each residue distinctly
color red, catalytic_ser
color blue, catalytic_asp
color orange, catalytic_his

# Zoom in on the active site
zoom catalytic_ser or catalytic_asp or catalytic_his, 8

# Set a clean white background for the saved image
bg_color white

# Save the image
png results/petase_structure.png, width=1200, height=1000, dpi=150, ray=1