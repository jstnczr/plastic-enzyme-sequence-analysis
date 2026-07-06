# Map engineered mutation sites onto wild-type PETase structure
# PDB ID: 6EQE - PETase from Ideonella sakaiensis

# Load the structure
fetch 6EQE

# Remove water molecules
remove solvent

# Basic display
bg_color white
hide everything
show cartoon
color grey80, all

# Show the catalytic triad for reference (Ser160, Asp206, His237)
select catalytic_triad, resi 160+206+237
show sticks, catalytic_triad
color red, catalytic_triad

# ThermoPETase mutations (Son et al. 2019): S121E, D186H, R280A
select thermo_mutations, resi 121+186+280
show spheres, thermo_mutations
color green, thermo_mutations

# FAST-PETase additional mutations (Lu et al. 2022): R224Q, N233K
select fast_unique, resi 224+233
show spheres, fast_unique
color purple, fast_unique

# DuraPETase mutations (Cui et al. 2021): 9 unique positions
select dura_unique, resi 117+119+140+159+165+168+180+188+214
show spheres, dura_unique
color orange, dura_unique

# R280A is the only mutation shared across all three variants
select shared_280, resi 280
color yellow, shared_280

# Zoom out to see the full protein with all mutation sites
zoom all

# Save image (results is one level up from scripts)
ray 1200, 900
png ../results/variant_mutations_mapped.png