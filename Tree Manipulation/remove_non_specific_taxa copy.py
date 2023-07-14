## Removes taxa with no species from dataset i.e. GENERA_sp.
import os

def remove_unspecified_species(filepath):
    removed_entries = []
    output_entries = []
    output_file = os.path.splitext(filepath)[0] + "_r.fas"

    output = ""

    with open(filepath, 'r') as fasta_file:
        header = ""
        for line in fasta_file:

            if line.startswith(">"):
                header = line.strip()
                if header.endswith("_sp."):
                    removed_entries.append(header.lstrip(">"))
                    header = ""
                else:
                    output += header + "\n"
            elif header:
                output += line
            
    # Write the removed entries to a file
    with open('Removed_entries.txt', 'w') as removed_file:
        for entry in removed_entries:
            removed_file.write(entry + '\n')

    # Write the edited fasta file
    with open(output_file, 'w') as output_fasta:
            output_fasta.write(output)

    return output_entries

# Usage example
filepath = 'COI-ND2.fas'
removed_entries = remove_unspecified_species(filepath)
