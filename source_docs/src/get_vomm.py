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
print(tree.babble('   ', 80, 4, topk = 2))
print(tree.babble('   ', 80, 4, topk = 2))
print(tree.babble('   ', 80, 4, topk = 2))
print(tree.babble('   ', 80, 4, topk = 2))
print(tree.babble('   ', 80, 4, topk = 2))
print(tree.babble('   ', 80, 4, topk = 2))
print(tree.babble('   ', 80, 4, topk = 2))
print(tree.babble('   ', 80, 4, topk = 2))

