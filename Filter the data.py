import pandas as pd

# File paths — update if needed
files = {
    "EC": "EC Raw Data.tsv",
    "PC": "PC Raw data.tsv",
    "HIP": "HP Raw data.tsv"
}

# Function to load and filter each dataset
def filter_deg(file_path, region):
    df = pd.read_csv(file_path, sep='\t')
    
    # Clean and convert columns
    df['adj.P.Val'] = pd.to_numeric(df['adj.P.Val'], errors='coerce')
    df['logFC'] = pd.to_numeric(df['logFC'], errors='coerce')
    df = df[df['adj.P.Val'].notna() & df['logFC'].notna()]
    
    # Filter DEGs
    filtered_df = df[(df['adj.P.Val'] < 0.05) & (df['logFC'].abs() > 1)].copy()
    
    # Save new file
    output_name = f"Filtered_{region}.csv"
    filtered_df.to_csv(output_name, index=False)
    print(f"{region}: {len(filtered_df)} significant genes saved to {output_name}")
    return filtered_df

# Run for each file
ec_filtered = filter_deg("EC Raw Data.tsv", "EC")
pc_filtered = filter_deg("PC Raw data.tsv", "PC")
hip_filtered = filter_deg("HP Raw data.tsv", "HIP")
