import pandas as pd

# Load filtered data
ec = pd.read_csv("/Users/farahyasser/Desktop/AD Project/Filtered_EC.csv")
pc = pd.read_csv("/Users/farahyasser/Desktop/AD Project/Filtered_PC.csv")
hip = pd.read_csv("/Users/farahyasser/Desktop/AD Project/Filtered_HIP.csv")

# Get sets
ec_genes = set(ec['Gene.symbol'].dropna())
pc_genes = set(pc['Gene.symbol'].dropna())
hip_genes = set(hip['Gene.symbol'].dropna())

# Find overlap
common = ec_genes & pc_genes & hip_genes

# Extract rows for common genes
ec_common = ec[ec['Gene.symbol'].isin(common)][['Gene.symbol', 'logFC', 'adj.P.Val']]
pc_common = pc[pc['Gene.symbol'].isin(common)][['Gene.symbol', 'logFC', 'adj.P.Val']]
hip_common = hip[hip['Gene.symbol'].isin(common)][['Gene.symbol', 'logFC', 'adj.P.Val']]

# Rename
ec_common.columns = ['Gene.symbol', 'logFC_EC', 'adj.P.Val_EC']
pc_common.columns = ['Gene.symbol', 'logFC_PC', 'adj.P.Val_PC']
hip_common.columns = ['Gene.symbol', 'logFC_HIP', 'adj.P.Val_HIP']

# Merge all
merged = ec_common.merge(pc_common, on='Gene.symbol').merge(hip_common, on='Gene.symbol')

# Add direction
merged['Direction_EC'] = merged['logFC_EC'].apply(lambda x: 'Upregulated' if x > 1 else 'Downregulated')
merged['Direction_PC'] = merged['logFC_PC'].apply(lambda x: 'Upregulated' if x > 1 else 'Downregulated')
merged['Direction_HIP'] = merged['logFC_HIP'].apply(lambda x: 'Upregulated' if x > 1 else 'Downregulated')

# Save with full path
output_path = "/Users/farahyasser/Desktop/AD Project/Common_DEGs_All_Regions.csv"
merged.to_csv(output_path, index=False)

print(f"✅ Saved {len(merged)} common genes to:")
print(output_path)
