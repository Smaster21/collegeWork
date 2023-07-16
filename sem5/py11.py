import time
start = time.time()
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()
#end = time.time()
print(time.time() - start)


###################################################################################################

import time
start = time.time()
def fibonacciSeries(i):
	if i <= 1:
		return i
	else:
		return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

num=10
if num <=0:
	print("Please enter a Positive Number")
else:
	print("Fibonacci Series:", end=" ")
for i in range(num):
	print(fibonacciSeries(i), end=" ")
	
print()
#end = time.time()
print(time.time() - start)

