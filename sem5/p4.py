import time
arr=input("Enter array elements : ")
arr=list(map(int,arr.split(",")))
print(arr)
wcount=0
fcount=0
start=time.time()
print("Array After Every Pass: ")
for i in range(1,len(arr)):
    fcount+=1
    key=arr[i]
    j=i-1
    while(j>=0 and arr[j]>key):
        wcount+=1
        arr[j+1]=arr[j]
        j=j-1
        arr[j+1]=key
        print(arr)
stop=time.time()
print("\nSorted Array: ",arr)
print("Execution Time: ",round((stop-start)*1000,5),"ms")
print("For Loop Executed ",fcount,"times")
print("While Loop Executed",wcount,"times")

#Best case :
import time
print("\nBest Case Problem!")
arr=[i for i in range(1,10001)]
wcount=0
fcount=021

start=time.time()
for i in range(1,len(arr)):
    fcount+=1
    key=arr[i]
    j=i-1
while(j>=0 and arr[j]>key):
    wcount+=1
    arr[j+1]=arr[j]
    j=j-1
    arr[j+1]=key
stop=time.time()
print("Execution Time: ",round((stop-start)*1000,5),"ms")
print("For Loop Executed ",fcount,"times")
print("While Loop Executed",wcount,"times")

#Average case :
import time
import random
print("\nAverage Case Problem!")
arr=[random.randint(1,10000) for i in range(1,10001)]
wcount=0
fcount=0
start=time.time()
for i in range(1,len(arr)):
    fcount+=1
    key=arr[i]
    j=i-1
while(j>=0 and arr[j]>key):
    wcount+=1
    arr[j+1]=arr[j]
    j=j-1
    arr[j+1]=key
stop=time.time()
print("Execution Time: ",round((stop-start)*1000,5),"ms")
print("For Loop Executed ",fcount,"times")
print("While Loop Executed",wcount,"times")

#Worst case :
import time
print("\nWorst Case Problem!")
arr=[i for i in reversed(range(1,10001))]
wcount=0
fcount=0
start=time.time()
for i in range(1,len(arr)):
    fcount+=1    
    key=arr[i]
    j=i-1
while(j>=0 and arr[j]>key):
    wcount+=1
    arr[j+1]=arr[j]
    j=j-1
    arr[j+1]=key
stop=time.time()
print("Execution Time: ",round((stop-start)*1000,5),"ms")
print("For Loop Executed ",fcount,"times")
print("While Loop Executed",wcount,"times")
