# Load required libraries
library(ape)
library(ggplot2)

# Read the aligned sequences
seqs <- read.FASTA("data/aligned_enzymes.fasta", type="AA")
seq_matrix <- as.matrix(seqs)

# Convert raw sequences to character matrix
char_matrix <- t(apply(seq_matrix, 1, function(x) strsplit(paste(rawToChar(x), collapse=""), "")[[1]]))
rownames(char_matrix) <- rownames(seq_matrix)

# Find conserved positions across PETase and serine hydrolases only
# (excluding alkB and MHETase as they are different enzyme families)
pet_cut_names <- c("PETase_Ideonella_sakaiensis", 
                   "Cutinase_Thermobifida_fusca", 
                   "Lipase_Thermonospora_curvata")

# Subset matrix to just these three enzymes
pet_cut_matrix <- char_matrix[pet_cut_names, ]

# Find positions where all three have the same amino acid and no gaps
conserved <- apply(pet_cut_matrix, 2, function(pos) {
  all(pos == pos[1]) && !any(pos == "-")
})

# Count and report conserved positions
num_conserved <- sum(conserved)
cat("Number of conserved positions across PETase and serine hydrolases:", num_conserved, "\n")
cat("Out of total alignment length:", ncol(char_matrix), "positions\n")
cat("Percentage conserved:", round(num_conserved/ncol(char_matrix)*100, 1), "%\n")

# Show which positions are conserved and what amino acid is there
conserved_positions <- which(conserved)
conserved_aas <- pet_cut_matrix[1, conserved]

cat("\nConserved positions and amino acids:\n")
for(i in 1:length(conserved_positions)){
  cat("Position", conserved_positions[i], ":", conserved_aas[i], "\n")
}

# Plot conservation across the alignment
conservation_score <- apply(pet_cut_matrix, 2, function(pos) {
  if(any(pos == "-")) return(0)
  max(table(pos)) / length(pos)
})

# Create dataframe for plotting
plot_data <- data.frame(
  position = 1:ncol(char_matrix),
  conservation = conservation_score
)

# Plot conservation profile
p <- ggplot(plot_data, aes(x=position, y=conservation, 
                           fill=conservation == 1.0)) +
  geom_col(width=1) +
  scale_fill_manual(values=c("FALSE"="steelblue", "TRUE"="darkred"),
                    labels=c("Partially conserved", "Fully conserved"),
                    name="") +
  labs(title="Conserved Residues Across PET-Degrading Serine Hydrolases",
       x="Alignment Position",
       y="Conservation Score (1.0 = fully conserved)") +
  theme_minimal() +
  theme(legend.position="top")

# Save plot
ggsave("results/conservation_profile.png", p, width=12, height=5, dpi=150)
cat("\nConservation profile saved to results/conservation_profile.png\n")