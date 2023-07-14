import re
from ete3 import Tree

## Script to rename tip labels in Kuhl et al tree

# Modify ordering of labels
def modify_tip_labels(tree):
    for leaf in tree.iter_leaves():
        label = leaf.name.split("_")
        print(label)
        family = label[5]
        leaf.name = f"{family}_{label[0]}_{label[1]}"
        
# read newick file
def read_newick(filename):
    with open(filename, 'r') as f:

        newick_format = f.readline()
        return newick_format

# Remove bootstrap labels
def drop_bootstrap_labels(newick_string):
    # Regular expression pattern to match bootstrap labels
    pattern = r':\d+(\.\d+)?'

    # Remove bootstrap labels from the Newick string
    modified_newick = re.sub(pattern, '', newick_string)

    return modified_newick

#Write file 
def write_newick(filename, newick_format):
        fs = open(filename, "w")

        fs.write(newick_format)

        fs.close()

def main():
    newick_string = read_newick("3UTR454-F100.rooted.fullnames.tre")
    tree = Tree(newick_string, format=1)
    modify_tip_labels(tree)
    modified_newick = tree.write(format=1)
    modified_newick = drop_bootstrap_labels(modified_newick)
    # print(modified_newick)
    write_newick("3UTRTree.tre", modified_newick)

# Run Script
if __name__ == '__main__':
    main()

