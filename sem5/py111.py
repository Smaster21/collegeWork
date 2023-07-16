import math
import time
start = time.time()
a = 10
b = 4
c= math.gcd(a,b)
print("The GCD of 10 and 4 is :", c)
#end = time.tim()
print(time.time() - start)

import time 
start = time.time()
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

print("The GCD of 10 and 4 is :", GCD(10,4))
#end = time.time()
print(time.time() - start)