#!/usr/bin/python

# Generate original static file to another with new prefix
# ./sgen index.html old_prefix static_index.html new_prefix


import sys
from os import walk, path

# File lists
# The two file lists should be aligned.

files = []
for (dirpath, dirname, filenames) in walk("../static"):
    for f in filenames:
        if ".html" in f:
            files.append(dirpath + "/" + f)

# prefix of target files
target_prefix = "../docs"
target_files = []
for f in files:
    target_files.append(f.replace("../static", target_prefix))
print(target_files)

# Variables of parsing

def parse_args():
    if len(sys.argv) < 3:
        print ("Not enough arguments")
        exit(1)
    original_prefix = sys.argv[1]
    new_prefix = sys.argv[2]
    # unsafe checkout prefix
    if original_prefix[0] != 'h' or original_prefix[-1] != '/' or new_prefix[0] != 'h' or new_prefix[-1] != '/':
        print ("Seems something wrong on the prefix")
        exit(1)
    return original_prefix, new_prefix

def sgen():
    original_prefix, new_prefix = parse_args()

    # parse the publications_ref into the appropriate html format

    for i in range(len(files)):
	    with open(files[i]) as f:
		    content = f.read()
		    new_content = content.replace(original_prefix, new_prefix)
	    with open(target_files[i], "w+") as f:
		    f.write(new_content)

sgen()