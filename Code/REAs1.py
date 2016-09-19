# Regular Expressions - Assignment 1
# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.

# The basic outline of this problem is to read the file, look for integers 
# using the re.findall(), looking for a regular expression of '[0-9]+' and 
# then converting the extracted strings to integers and summing up the integers.

import re

fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
    #fname = "regex_sum_sample.txt"
    fname = "regex_sum_actual.txt"

fh = open(fname)
numList = list()
for line in fh :
    line.rstrip()
    lst = re.findall('[0-9]+',line)
    if len(lst) == 0 : continue

    for num in lst:
        numList.append(int(num))

print 'sum =',sum(numList)