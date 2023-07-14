# Tree Manipulation Scripts

## add_family_name.py

Input: Treefile, Taxonomy csv
Output: Modified Treefile

Takes a treefile with tips in the format `Genus_species` and formats the tip labels to `Family_Genus_species` using the provided taxonomy file. Taxonomy file must include a column for `Tip` and `Family`.

#### Usage:
Replace TAXONOMY_CSV and TREEFILE variables with the path to files.

