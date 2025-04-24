import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Load the cleaned list of common DEGs
df = pd.read_csv("Cleaned_Common_DEGs_Unique.csv")

# Get sets of downregulated genes by brain region
ec_down = set(df[df['Direction_EC'] == 'Downregulated']['Gene.symbol'])
pc_down = set(df[df['Direction_PC'] == 'Downregulated']['Gene.symbol'])
hip_down = set(df[df['Direction_HIP'] == 'Downregulated']['Gene.symbol'])

# Plot Venn diagram
plt.figure(figsize=(7, 7))
venn3(
    [ec_down, pc_down, hip_down],
    set_labels=('EC', 'PC', 'HIP')
)
plt.title("Consistently Downregulated Genes Across Brain Regions")
plt.tight_layout()
plt.savefig("Venn_Downregulated_Genes.png", dpi=300)
plt.show()

print("✅ Saved Venn diagram as 'Venn_Downregulated_Genes.png'")
