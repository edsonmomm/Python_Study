# tuple 
# Get the top 10 most common words
fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
    fname = "romeo.txt"

fh = open(fname)
counts = dict()

for line in fh :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items() :
    lst.append((val, key))

lst.sort(reverse=True)

for val, key in lst[:10]:
    print key, val