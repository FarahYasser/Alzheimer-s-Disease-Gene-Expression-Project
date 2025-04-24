import pandas as pd

# Load your cleaned full common DEG list (620 genes)
df = pd.read_csv("Cleaned_Common_DEGs_Unique.csv")

# Filter for consistently regulated genes across all 3 regions
consistent = df[
    ((df['Direction_EC'] == 'Upregulated') &
     (df['Direction_PC'] == 'Upregulated') &
     (df['Direction_HIP'] == 'Upregulated')) |
    ((df['Direction_EC'] == 'Downregulated') &
     (df['Direction_PC'] == 'Downregulated') &
     (df['Direction_HIP'] == 'Downregulated'))
]

# Select relevant columns: expression + p-value + direction
columns_to_keep = [
    'Gene.symbol',
    'logFC_EC', 'adj.P.Val_EC', 'Direction_EC',
    'logFC_PC', 'adj.P.Val_PC', 'Direction_PC',
    'logFC_HIP', 'adj.P.Val_HIP', 'Direction_HIP'
]
consistent = consistent[columns_to_keep]

# Save to CSV
output_path = "Consistent_DEGs_Expression_and_Pval.csv"
consistent.to_csv(output_path, index=False)

print(f"✅ Saved {len(consistent)} consistent genes to {output_path}")
