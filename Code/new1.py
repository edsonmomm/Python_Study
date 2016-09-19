import urllib
from BeautifulSoup import *
import re

def retrieveTags(pURL):
    html = urllib.urlopen(pURL).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    anchorTags = soup('a')
    return anchorTags

url = raw_input('Enter - ')
pos = int(raw_input('Enter Position:'))
count = int(raw_input('Enter Count: '))

print url
# Loop "count" times and get the link at position "pos"
for c in range(count):
    tags = retrieveTags(url)

    url = tags[pos-1].get('href', None)
    print url
