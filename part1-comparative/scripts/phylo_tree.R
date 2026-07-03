# Load required libraries
library(ape)

# Read alignment as amino acid sequences
seqs <- read.FASTA("data/aligned_enzymes.fasta", type="AA")

# Convert to matrix and calculate distance
seq_matrix <- as.matrix(seqs)
dist_matrix <- dist.aa(seq_matrix)

# Build Neighbor-Joining tree
tree <- nj(dist_matrix)

# Root the tree using alkB as outgroup
tree <- root(tree, outgroup="alkB_Pseudomonas_oleovorans", resolve.root=TRUE)

# Bootstrap BEFORE renaming labels
boot <- boot.phylo(tree, seq_matrix, function(x) root(nj(dist.aa(x)), 
                                                      outgroup="alkB_Pseudomonas_oleovorans", resolve.root=TRUE),B=1000)

# Clean up tip labels AFTER bootstrap
tree$tip.label <- gsub("_", " ", tree$tip.label)
tree$tip.label <- gsub("Ideonella sakaiensis", "(I. sakaiensis)", tree$tip.label)
tree$tip.label <- gsub("Thermobifida fusca", "(T. fusca)", tree$tip.label)
tree$tip.label <- gsub("Thermonospora curvata", "(T. curvata)", tree$tip.label)
tree$tip.label <- gsub("Pseudomonas oleovorans", "(P. oleovorans)", tree$tip.label)

# Define colours by enzyme family
tip_colours <- ifelse(grepl("PETase|Cutinase|Lipase", tree$tip.label), "steelblue",
                      ifelse(grepl("alkB", tree$tip.label), "darkred", "darkorange"))

# Save tree as image
png("results/phylogenetic_tree.png", width=1600, height=900, res=150)
plot(tree,
     main="Phylogenetic Tree of Plastic-Degrading Enzymes",
     cex=0.8,
     tip.color=tip_colours,
     edge.width=2,
     label.offset=8)

# Add bootstrap values
nodelabels(boot, cex=0.7, frame="none", adj=c(1.2, -0.3))

# Add legend
legend("right",
       legend=c("PETase/Cutinase/Lipase (serine hydrolases)", 
                "MHETase", 
                "alkB (alkane hydroxylase)"),
       text.col=c("steelblue", "darkorange", "darkred"),
       bty="n",
       cex=0.7)

dev.off()

print("Phylogenetic tree saved to results/phylogenetic_tree.png")