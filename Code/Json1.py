# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to 
# http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, 
# read the JSON data from that URL using urllib and then parse and extract the 
# comment counts from the JSON data, compute the sum of the numbers in the file
# and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give 
# you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json (Sum=2553)
# Actual data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_170865.json (Sum ends with 72)
# You do not need to save these files to your folder since your program will read 
# the data directly from the URL. Note: Each student will have a distinct data url 
# for the assignment - so only use your own data url for analysis.
# Data Format
# The data consists of a number of names and comment counts in JSON as follows:
# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }
# The closest sample code that shows how to parse JSON and extract a list 
# is json2.py. You might also want to look at geoxml.py to see how to 
# prompt for a URL and retrieve data from a URL.

import urllib
import json

#url = raw_input('Enter - ')
#url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json"
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_170865.json"
print "Retrieving", url

jsonFile = urllib.urlopen(url).read()
print "Retrieved", len(jsonFile), "characters"

summary = list()

info = json.loads(jsonFile)
for item in info['comments']:
#    print 'Name:', item['name']
#    print 'Count:', item['count']
    summary.append(item['count'])

print "Count:", len(summary)
print "Sum", sum(summary)