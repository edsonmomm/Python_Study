#Exercise Lists
# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() function. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already 
# in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

fh = open('romeo.txt')
lst = list()
for line in fh:
    line.rstrip()

    for word in line.split():
        if word not in lst:
            lst.append(word)

if len(lst) > 0:
    lst.sort()
    print lst