import urllib
import json

url = raw_input('Enter - ')
print "Retrieving", url

jsonFile = urllib.urlopen(url).read()
print "Retrieved", len(jsonFile), "characters"

summary = list()

info = json.loads(jsonFile)
for item in info['comments']:
    summary.append(item['count'])

print "Count:", len(summary)
print "Sum", sum(summary)