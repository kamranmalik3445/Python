# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages. You can pull the hour out from the 'From '
# line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file name: ")
fh = open(fname)

hourDict = dict()

for line in fh:
    if not line.startswith('From '):
        continue
    email = line.split()
    hour = email[5].split(':')
    h = hour[0]
    hourDict[h] = hourDict.get(h, 0) + 1

myList = list()

for k, v in hourDict.items():
    data = k,v
    myList.append(data)

for k, v in sorted(myList):
    print(k, v)
