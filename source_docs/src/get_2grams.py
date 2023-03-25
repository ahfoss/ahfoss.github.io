from collections import defaultdict
import csv 

#dirname = "../gutenberg/"
#basename = "room_with_a_view"
dirname = "../codenet/"
basename = "cpp_raw"
inname = "./" + dirname + basename + ".txt"

fid = open(inname, 'r')

dat = fid.readlines()

# Extract 2-grams
gram_dict = defaultdict(lambda: 0)

for i,line in enumerate(dat):
    for j,_ in enumerate(line):
        gram = line[j:j+2]
        gram_dict[gram] += 1
#    if i > 3:
#        break

# Write 2-grams into 3 vectors:
# - Letter 1
# - Letter 2
# - Count
letter1 = []
letter2 = []
count = []

for item in gram_dict.items():
    if len(item[0]) > 1:
        letter1.append(item[0][0])
        letter2.append(item[0][1])
        count.append(item[1])

rows = [[l1, l2, c] for c,l1,l2 in sorted(zip(count, letter1, letter2),reverse=True)]

# field names 
fields = ['L1','L2','Count']
    
# name of csv file 
outname = dirname + basename + ".csv"
    
# writing to csv file 
with open(outname, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile, escapechar = "\\") 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)
