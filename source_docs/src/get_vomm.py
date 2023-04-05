# TODO: Remove main characters' names, or use multiple books?
from Vomm import Tree

dirname = "../gutenberg/"
basename = "room_with_a_view"
#dirname = "../codenet/"
#basename = "cpp_raw"
inname = "./" + dirname + basename + ".txt"

stride = 5

fid = open(inname, 'r')

dat = fid.readlines()

tree = Tree()
for i,line in enumerate(dat):
    for indx in range(len(line)-stride):
        tree.update(line[indx:(indx+stride)])

#tree.print()
nchar = 80
context = 6
# topk 2ish seems good for starters?
# even topk 8ish seems to get decent variety.
topk = 2

print(tree.babble('   ', nchar, context, topk))
print(tree.babble('   ', nchar, context, topk))
print(tree.babble('   ', nchar, context, topk))
print(tree.babble('   ', nchar, context, topk))
print(tree.babble('   ', nchar, context, topk))
print(tree.babble('   ', nchar, context, topk))
print(tree.babble('   ', nchar, context, topk))
print(tree.babble('   ', nchar, context, topk))

