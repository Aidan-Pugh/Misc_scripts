## Script to replace tips in form Genus_species with Family_genus_species

TAXONOMY_CSV="TaxaDataEdit.csv"
TREEFILE="partitions.nex.contree"

import pandas as pd

def get_family_name(searchTerm, df):

    row = df[df['Tip'] == searchTerm]

    if len(row) != 1:
        raise ValueError(searchTerm + " not found in csv!")

    for index, row in row.iterrows():
        return row['Family']

print("Reading input files...")

# Read Newick Tree File
with open(TREEFILE, 'r') as f:
    tree = f.read()

print("Read " + TREEFILE + ".")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(TAXONOMY_CSV)

print("Read " + TAXONOMY_CSV + ".")

print("Replacing Tips...")

count = 0
modifiedFile = tree

for index, row in df.iterrows():

    try:
        modifiedFile = modifiedFile.replace(row['Tip'], row['Family'] + "_" + row['Tip'])
    except:
        print("Could not replace tip")
        print(index)
        print(row)
    count += 1
    if count % 500 == 0:
        print(f"Read {count} tips from taxonomy...")

print(f"Done. Read {count} tips total.")

print("Writing to file...")

with open(TREEFILE + "_family.tre", "w") as f:
    f.write(modifiedFile)

print("Script complete.")