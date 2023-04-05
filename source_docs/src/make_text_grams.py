import sys
import random
from collections import defaultdict

# TODO: https://github.com/rpgomez/vomm

if len(sys.argv) < 4:
    raise Exception('Need at least 3 arguments.')
if sys.argv[1] == 'room':
    dirname = '../gutenberg/'
    basename = 'room_with_a_view'
elif sys.argv[1] == 'cpp':
    dirname = '../codenet/'
    basename = 'cpp_raw'

# Note you should never start at line 0 (the column names).
startline = int(sys.argv[2])
endline = int(sys.argv[3])
if startline <= 0:
    raise Exception('Startline must be greater than 0.')
if startline >= endline:
    raise Exception('Startline must be strictly less than endline.')

inname = './' + dirname + basename + '.csv'


# interesting settings: 1-1000: most letters, some caps & punctuation.
#   --- too normal.
# 1-200, 200-400, 400-600?
# or perhaps increments of 300?
# Also small increments of 20.

fid = open(inname, 'r')

undesired_chars = ['\x00']
# Get specified 2grams
gramlist = []
for position, line in enumerate(fid):
    if position >= startline and position <= endline:
        cleanedline = line.strip()
        # Skip lines with non-ascii code.
        try:
            cleanedline.encode('ascii')
        except UnicodeEncodeError:
            pass
        else:
            tup = tuple(cleanedline.split(','))
            # Avoid undesired chars.
            if not (tup[0] in undesired_chars or tup[1] in undesired_chars):
                if len(tup) == 3: # ignore missing entries.
                    gramlist.append(tup)
    elif position > endline:
        break

# Make sampling structure
tmp_letters1 = [] # set if memory gets too large
tmp_letters2 = defaultdict(lambda: []) # lambda: set() if memory gets too large
for elm in gramlist:
    tmp_letters1.append(elm[0])
    tmp_letters2[elm[0]].append(elm[1])

letters1 = ''.join(sorted(list(set(tmp_letters1))))
letters2 = {}
for kk in tmp_letters2.keys():
    letters2[kk] = ''.join(sorted(list(set(tmp_letters2[kk]))))

#print(letters1)
#print(letters2)
del(tmp_letters1)
del(tmp_letters2)

# Generate nline lines of nsamp letters.
nline = 10
nsamp = 30
max_word_len = 6

numlet = 0
reg2 = ['a','b']
for i in range(nline):
    # Seed this line.
    outstr = random.choice(letters1)
    for j in range(nsamp):
        latest = outstr[len(outstr)-1]
        try:
            new = random.choice(letters2[latest])
        except KeyError:
            new = random.choice(letters1)
        # Don't allow words longer than max_word_len.
        if new == ' ':
            numlet = 0
        else:
            numlet += 1
        if numlet >= max_word_len:
            new = ' '
            numlet = 0
        # Don't print any triples.
        if reg2[0] == new:
            if reg2[1] == new:
                #print('TRIPLE: ' + ''.join(reg2) + new)
                continue
        # Append selected letter to string.
        outstr += new
        # Update the 2-back registry.
        reg2.append(new)
        _ = reg2.pop(0)
    print(outstr)
