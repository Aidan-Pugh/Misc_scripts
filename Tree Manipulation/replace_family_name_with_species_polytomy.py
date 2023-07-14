# Script to replace family names in backbone tree with species polytomies

import pandas as pd

import newick

print("Reading backbone tree...")

# Read Newick Tree File
with open("bbbbbbb", 'r') as f:
    treeNewick = f.read()

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('TaxaDataEdit.csv')

# Create a list of families
families = treeNewick.replace(")", "")
families = families.replace("(", "")
families = families.replace(";", "")
families = families.replace(" ", "")
families = families.split(",")
count = 0

# Check if anything is missing from the newick tree that is contained within the csv

missing_families = df[~df['Family'].isin(families)]

if len(missing_families) > 0:
    print("Some families are missing from the tree:")
    for index, row in missing_families.iterrows():
        print(f"{row['Tip']} in {row['Family']}")

print("Starting Replacement.")

for family in families:

    # print(family)
    # print(treeNewick)

    #Get rows from df
    taxarows = df[df['Family'] == family]
    replacement = []

    #Create polytomy string
    if len(taxarows) < 1:
        print(f"No data for {family}.")
        continue
    
    # Loop through the rows and add the 'Tip' column
    for index, row in taxarows.iterrows():
        if str(row['Tip']).endswith('sp.') or str(row['Tip']).endswith('environmental'):
            print("Not incl. sp. or env taxa.")
        else:
            replacement.append(row['Tip'])
    
    #Perform replacement
    replacementString = (', '.join(replacement))

    # Check if single row
    if len(taxarows) == 1:
        treeNewick = treeNewick.replace(family, replacementString)
    else:
        treeNewick = treeNewick.replace(family, "(" + replacementString + ")")
    
    # print(treeNewick)
    
    count += 1

    if count % 20 == 0:
        print(f"Replaced {count} families in newick tree file...")

print(f"Done. Replaced {count} families with species polytomies.")



# Write to file

print("Writing to new tree file...")

with open("backbone_species_tree3.tre", "w") as f:
    f.write(treeNewick)

print("Script Complete.")

        
    