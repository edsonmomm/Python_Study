# Following Links in Python
# In this assignment you will write a Python program that expands on 
# http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read 
# the HTML from the data files below, extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position from the top and follow that link 
# and repeat the process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the 
# name for your testing and the other is the actual data you need to process for the assignment

# Sample problem: Start at http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. 
# Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah

# Actual problem: Start at: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Dion.html 
# Find the link at position 18 (the first name is 1). 
# Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# First character of last name in sequence: N

# Strategy
# The web pages tweak the height between the links and hide the page after a few seconds 
# to make it difficult for you to do the assignment without writing a Python program. 
# But frankly with a little effort and patience you can overcome these attempts to make 
# it a little harder to complete the assignment without writing a Python program. 
# But that is not the point. The point is to write a clever Python program to solve the program.

import urllib
from BeautifulSoup import *
import re

def retrieveTags(pURL):
    html = urllib.urlopen(pURL).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    anchorTags = soup('a')
    return anchorTags

pos = int(raw_input('Enter Position:'))
count = int(raw_input('Enter Count: '))

#url = raw_input('Enter - ')
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Antonina.html"
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Dion.html"
print url
# Loop "count" times and get the link at position "pos"
for c in range(count):
    tags = retrieveTags(url)

    url = tags[pos-1].get('href', None)
    print url
    #name = re.findall("known_by_(.+).html", url)
    #print name[0]
