"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
#with open('texts.csv', 'r') as f: #uncomment it before submitting
with open('/Users/seungkukkim/Downloads/P0/texts.csv', 'r') as f:#delete before submitting
    reader = csv.reader(f)
    texts = list(reader)

#with open('calls.csv', 'r') as f: #uncomment it before submitting
with open('/Users/seungkukkim/Downloads/P0/calls.csv', 'r') as f:#delete before submitting
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
#declare an variable called count and assign 0
count=0
#create an dictionary that has key and value pair then iterate texts and calls
phoneNums={}
for arr in texts:
    for key in range(2):
        if arr[key] not in phoneNums:
            phoneNums[arr[key]]=1
            count=count+1


for arr in calls:
    for key in range(2):
        if arr[key] not in phoneNums:
            phoneNums[arr[key]]=1
            count=count+1
            #print(arr[key])

#if the number doesn't exist add the key and set the value to 1 and increment count
#after iteration print "There are <count> different telephone numbers in the records."
print("There are " +str(count)+ " different telephone numbers in the records.")
#print(calls[0])
