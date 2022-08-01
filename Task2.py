"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
#with open('texts.csv', 'r') as f:
with open('/Users/seungkukkim/Downloads/P0/texts.csv', 'r') as f:#delete before submitting
    reader = csv.reader(f)
    texts = list(reader)

#with open('calls.csv', 'r') as f:
with open('/Users/seungkukkim/Downloads/P0/calls.csv', 'r') as f:#delete before submitting
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
#declare an empty dictionary
phoneNumTotalTime={}
#declare an dictionary with telephone number as the key and the longest time as the variable
longest=[]
num=calls[0][0]
time=int(calls[0][3])
longest.append(num)
longest.append(time)

print(longest)
#iterate the calls
for arr in calls:
#if the number is not a key in dictionary add the number as the key in dictionary
#and time spent as the value in which the index is 3
#else add the time spent to the values of two phone numbers
    phoneNum1=arr[0]
    phoneNum2=arr[1]
    total=int(arr[3])
    if phoneNum1 not in phoneNumTotalTime:
        phoneNumTotalTime[phoneNum1]=int(total)
        if int(phoneNumTotalTime[phoneNum1])>int(longest[1]):
            longest[0]=phoneNum1
            longest[1]=total
    else:
        phoneNumTotalTime[phoneNum1]=int(phoneNumTotalTime[phoneNum1])+int(total)
        if int(phoneNumTotalTime[phoneNum1])>int(longest[1]):
            longest[0]=phoneNum1
            longest[1]=int(phoneNumTotalTime[phoneNum1])
    if phoneNum2 not in phoneNumTotalTime:
        phoneNumTotalTime[phoneNum2]=int(total)
        if int(phoneNumTotalTime[phoneNum1])>int(longest[1]):
            longest[0]=phoneNum1
            longest[1]=int(phoneNumTotalTime[phoneNum1])
    else:
        phoneNumTotalTime[phoneNum2] =int(phoneNumTotalTime[phoneNum2]) + int(total)
        if int(phoneNumTotalTime[phoneNum1])>int(longest[1]):
            longest[0]=phoneNum1
            longest[1]=int(phoneNumTotalTime[phoneNum1])
print(longest[0]+" spent the longest time, "+str(longest[1])+" seconds, on the phone during"+
" September 2016.")
