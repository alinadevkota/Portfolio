import pandas as pd

# Read TSV
tsv_file = 'publications.tsv'
df = pd.read_csv(tsv_file, sep='\t')

# Save as CSV
csv_file = 'publications.csv'
df.to_csv(csv_file, index=False)
