import pandas as pd

# Load the common genes file
df = pd.read_csv("Common_DEGs_All_Regions.csv")

# Calculate the average adjusted p-value across regions
df['avg_p'] = df[['adj.P.Val_EC', 'adj.P.Val_PC', 'adj.P.Val_HIP']].mean(axis=1)

# Keep only the best row (lowest avg p) per gene
df_deduplicated = df.sort_values('avg_p').drop_duplicates(subset='Gene.symbol', keep='first')

# Drop the helper column
df_deduplicated = df_deduplicated.drop(columns=['avg_p'])

# Save cleaned file
df_deduplicated.to_csv("Cleaned_Common_DEGs_Unique.csv", index=False)

# Summary
print(f"✅ Saved {len(df_deduplicated)} unique genes to 'Cleaned_Common_DEGs_Unique.csv'")
