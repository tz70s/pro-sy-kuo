#!/usr/bin/python

# parse the publications_ref into the appropriate html format
with open("./data/publications_ref.txt") as f:
    content = f.readlines()
f.close()

content = [x.strip() for x in content] 

with open("./data/publications_ref.html", 'w') as f:
    for line in content:
        if line == "":
            continue
        if line[0] != '[':
            f.write("<hr>\n<h4 class=\"navar-header\">" + line + "</h4>\n")
            continue
        f.write("<p class=\"navar-text\">" + line + "</p>\n")
f.close()

# parse the publications_ref into the appropriate html format
with open("./data/award_ref.txt") as f:
    content = f.readlines()
f.close()

content = [x.strip() for x in content] 

with open("./data/award_ref.html", 'w') as f:
    for line in content:
        if line == "":
            continue
        f.write("<li>" + line + "</li>\n")
f.close()

# parse the editorship_ref into the appropriate html format
with open("./data/editorship_ref.txt") as f:
    content = f.readlines()
f.close()

content = [x.strip() for x in content] 

with open("./data/editorship_ref.html", 'w') as f:
    for line in content:
        if line == "":
            continue
        f.write("<li>" + line + "</li>\n")
f.close()

# parse the activity_ref into the appropriate html format
with open("./data/activity_ref.txt") as f:
    content = f.readlines()
f.close()

content = [x.strip() for x in content] 

with open("./data/activity_ref.html", 'w') as f:
    for line in content:
        if line == "":
            continue
        f.write("<li>" + line + "</li>\n")
f.close()


