## Script to colour tips by families

import colorsys
import pandas as pd
import random
import time

family_in_tip = True

# Generate n colour combinations
def generate_color_combinations(n):
    colors = []
    for i in range(n):
        hue = i / n  # Vary the hue value for each color combination
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV color to RGB
        hex_code = '#%02x%02x%02x' % (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        colors.append(hex_code)
    return colors

def get_family_name(searchTerm, df):

    row = df[df['Tip'] == searchTerm]

    if len(row) != 1:
        raise ValueError(searchTerm + " not found in csv!")

    for index, row in row.iterrows():
        return row['Family']


# Read Newick Tree File
with open("partitions_family.contree", 'r') as f:
    nexusFile = f.read()

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('TaxaDataEdit.csv')
df = df.sort_values(by=['Order'], ascending=False)

# Generate unique colours for each family

families = df['Family'].unique()

colours = generate_color_combinations(len(families))
# random.shuffle(colours)

family_colour = {}

for i in range(len(families)):
    family_colour[families[i]] = colours[i]

lines = nexusFile.splitlines()
replacement = False

for i, line in enumerate(lines):
    if "taxlabels" in line:
        print("Setting tip colours...")
        replacement = True
        continue
    elif replacement and ";" in line:
        print("Finished setting tip colours.")
        replacement = False
        break

    if replacement:

        taxonname = line.replace("\t", "")
    
        if taxonname.startswith("'"):
            search = taxonname.replace("'", "")
        else:
            search = taxonname
        
        try:
            if family_in_tip:
                family = search.split("_")[0]
                # print(family)
            else:
                family = get_family_name(search, df)
            
            modified_line = line.replace(taxonname, taxonname + "[&!color=" + family_colour[family] + "]")
            lines[i] = modified_line
        except:
            print(f"Could not replace for taxon: {taxonname} with family: {family}")
            print(line)
            
    # time.sleep(0.5)

# print(lines[0:20])
print("Writing to new file...")

content = "\n".join(lines)

with open("partitions_family_Coloured1.tre", 'w') as f:
    f.write(content)

print("Wrote to file. Script finished.")


#[&!color=#ff3333]