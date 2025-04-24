# Alzheimer's Disease Gene Expression Project

This project explores differentially expressed genes (DEGs) across three Alzheimer’s-affected brain regions: the **entorhinal cortex (EC)**, **hippocampus (HIP)**, and **posterior cingulate cortex (PC)**. The goal was to identify genes that are **consistently dysregulated** in all three regions and understand their functional roles through enrichment analysis and visualization.

---

## Background
Alzheimer’s disease is marked by progressive cognitive decline and is associated with region-specific molecular changes. By analyzing three brain regions known to be affected early in AD, this project aims to:

- Identify overlapping and consistently dysregulated genes
- Visualize gene expression patterns
- Functionally annotate shared dysregulation through pathway analysis

---

## Methods

- **Data source**: Gene Expression Omnibus (GEO)
- **Filtering criteria**: Adjusted p-value < 0.05 and |log2FC| > 1
- **Tools used**: Python (Pandas, Matplotlib, Seaborn), g:Profiler

### Analytical Workflow
1. Filtering DEGs in EC, PC, and HIP
2. Identifying genes common to all regions
3. Isolating consistently dysregulated genes
4. Creating volcano plots, heatmaps, and Venn diagrams
5. Running functional enrichment analysis (GO:BP, KEGG, Reactome)

Requirements:
pandas
matplotlib
seaborn
numpy
matplotlib-venn
gprofiler-official

---

## Results

### DEG Filtering
- EC: 5,665 significant DEGs
- PC: 10,494 significant DEGs
- HIP: 5,330 significant DEGs

### Shared & Consistent DEGs
- 620 genes were shared across EC, PC, and HIP
- A subset of genes were consistently upregulated or downregulated in all three regions

### Functional Enrichment Highlights

| Region | Key Pathways |
|--------|---------------|
| EC     | Glial activation, NF-kB signaling, cytokine-mediated immune response |
| HIP    | Amyloid-beta response, apoptosis, microglial activation |
| PC     | T cell signaling, synapse organization, axonogenesis |

> All regions showed enrichment in oxidative stress and inflammatory signaling.

---

## Visualizations

All visualizations generated during this project are located in the `figures/` directory:

- Volcano plots per region
- Heatmap of consistently dysregulated genes
- Venn diagrams of up/downregulated DEGs
- Enrichment bar plots (individual and combined)

---

## Interpretation

This analysis reaffirmed known molecular mechanisms of Alzheimer’s disease using a reproducible and systematic approach. Each brain region displayed distinct yet overlapping expression patterns:

- **EC**: Early immune activation and cytokine signaling suggest it may initiate AD pathology.
- **HIP**: Strong inflammatory signals and apoptotic processes point to intense degenerative pressure.
- **PC**: Immune-related T cell activation and neuronal remodeling imply both vulnerability and adaptive responses.

Despite their differences, all three regions share core dysregulation of oxidative stress and inflammatory processes — highlighting these as foundational to AD progression.

---

## Future Work

- Perform functional enrichment on region-unique DEGs
- Integrate RNA-seq or single-cell RNA-seq datasets
- Investigate cell-type specific gene signatures

---

## Author

**Farah Yasser**  
Medical Student

---

## License

This project is licensed for academic and educational use. Please credit the author if you build upon or reuse any part of this work.
