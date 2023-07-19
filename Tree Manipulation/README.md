# Tree Manipulation Scripts

## add_family_name.py

    Input: Treefile, Taxonomy csv
    Output: Modified Treefile

Takes a treefile with tips in the format `Genus_species` and formats the tip labels to `Family_Genus_species` using the provided taxonomy file. Taxonomy file must include a column for `Tip` and `Family`.

#### Usage:
Replace `TAXONOMY_CSV` and `TREEFILE` variables with the path to files.
Run with python3 in folder containing both files.

## check_family_names.py

    Input: Taxonomy csv, Tip list (as string)
    Output: Discrepencies between family list and those in the taxonomy file.

Takes a taxonomy csv and a list of tips and informs via a terminal output as to whether there are tips that appear in the taxonomy not in the tree and vice versa. Compares to the `Family` column of a taxonomy file.

#### Usage:
Replace `TAXONOMY_CSV` with the path to the taxonomy file and replace `FAMILIES_LIST` with a list of families from the backbone tree seperated with spaces e.g. `Alligatoridae Crocodylidae Struthionidae Rheidae...`.
Run with python3 in folder containing the taxonomy csv file.

## colour_families.py

    Input: Treefile (Figtree edited), Taxonomy csv
    Output: Modified Figtree file

Takes a treefile that has been formatted with figtree and a taxonomy csv and colours the tips based on the family of the taxon at the tip. 