"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
list = []
dictC = set() #numbers that called other numbers
dictR = set() #set with received call numbers
dictST = set() #set with numbers that sent texts
dictRT = set() #set with num that received text
setTeleM = set()#set with telemarkter number
for num in calls:
  dictC.add(num[0])
  dictR.add(num[1])

for num in texts:
  dictST.add(num[0])
  dictST.add(num[1])

for num in dictC:
  if num not in dictST and num not in dictR:
    setTeleM.add(num)

#print(setTeleM)
for num in setTeleM:
  list.append(num)
list.sort();
print("These numbers could be telemarketers: ")
for num in list:
  print(num)
