# Write a program to read through the mbox-short.txt and figure out 
# who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those 
# lines as the person who sent the mail. The program creates a Python 
# dictionary that maps the sender's mail address to a count of the number 
# of times they appear in the file. After the dictionary is produced, the 
# program reads through the dictionary using a maximum loop to 
# find the most prolific committer.

name = raw_input("Enter file:")

if len(name) < 1 : 
    name = "mbox-short.txt"

handle = open(name)

# create a list with all the senders
senders = list()
for line in handle:
    line.rstrip()
    
    if line.startswith('From:') : continue
    if line.startswith('From') : 
        lineList = line.split()
        senders.append(lineList[1])

# count the senders
senderDict = dict()
for sender in senders:
    senderDict[sender] = senderDict.get(sender,0) + 1

# finds the sender with more mail
BigSender = None
amoutMail = None
for sender,MailQtd in senderDict.items() :
    if BigSender is None:
        BigSender = sender
        amoutMail = MailQtd
    else:
        if MailQtd > amoutMail :
            BigSender = sender
            amoutMail = MailQtd

print BigSender, amoutMail