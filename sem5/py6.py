Coins = [500,100,50,20,10,1]
n = 732
s = []
for i in Coins:
	while i <= n:
		s.append(i)
		n = n-i
print("The number of coins used is :",s)