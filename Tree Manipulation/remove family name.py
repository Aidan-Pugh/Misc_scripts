import re

from ete3 import Tree

def modify_tip_labels(tree):
    for leaf in tree.iter_leaves():
        label = leaf.name.split("_")
        family = label[0]
        leaf.name = f"{family}"
        if leaf.name == "":
            print("error")
            print(label)

def read_newick(filename):
    with open(filename, 'r') as f:

        newick_format = f.readline()
        return newick_format

def drop_bootstrap_labels(newick_string):
    # Regular expression pattern to match bootstrap labels
    pattern = r':\d+(\.\d+)?'

    # Remove bootstrap labels from the Newick string
    modified_newick = re.sub(pattern, '', newick_string)

    return modified_newick

def main():
    newick_string = read_newick("3UTRFamilyTree.phy")
    tree = Tree(newick_string, format=1)
    modify_tip_labels(tree)
    modified_newick = tree.write(format=1)
    # modified_newick = drop_bootstrap_labels(modified_newick)
    # print(modified_newick)
    write_newick("3UTRFamilytree.tre", modified_newick)

def write_newick(filename, newick_format):
        fs = open(filename, "w")

        fs.write(newick_format)

        fs.close()

if __name__ == '__main__':
    main()

