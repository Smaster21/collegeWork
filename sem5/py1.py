import time
start = time.time()
num = 5 
factorial = 1
if num < 0:
   print("ERROR")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is:",factorial)
#end = time.time()
print(time.time() - start)
##############################################################################################################
import time
start = time.time()
num = 5
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)       
if num < 0:
   print("ERROR")
else:
   print("The factorial of", num, "is:", factorial(num))
#end = time.time()
print(time.time() - start)
