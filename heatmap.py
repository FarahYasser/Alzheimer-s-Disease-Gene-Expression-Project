
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned common genes file
df = pd.read_csv("Cleaned_Common_DEGs_Unique.csv")

# Filter for consistently regulated genes
consistent_df = df[
    ((df['Direction_EC'] == 'Upregulated') &
     (df['Direction_PC'] == 'Upregulated') &
     (df['Direction_HIP'] == 'Upregulated')) |
    ((df['Direction_EC'] == 'Downregulated') &
     (df['Direction_PC'] == 'Downregulated') &
     (df['Direction_HIP'] == 'Downregulated'))
].copy()

# Prepare data
heatmap_data = consistent_df[['Gene.symbol', 'logFC_EC', 'logFC_PC', 'logFC_HIP']]
heatmap_data.set_index('Gene.symbol', inplace=True)

# Plot and save
plt.figure(figsize=(12, max(10, 0.3 * len(heatmap_data))))
sns.heatmap(
    heatmap_data,
    cmap='vlag',
    center=0,
    annot=False,
    linewidths=0.5,
    linecolor='grey'
)
plt.title("Heatmap of Consistently Regulated Genes Across Brain Regions")
plt.xlabel("Brain Region")
plt.ylabel("Gene Symbol")
plt.tight_layout()

# Save as PNG
plt.savefig("Consistent_Genes_Heatmap.png", dpi=300)
print("✅ Heatmap saved as 'Consistent_Genes_Heatmap.png'")
plt.close()
