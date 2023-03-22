with open ('C:/SAFU MASTER/sem4/pyy.txt') as f1:
	n=int(input("Enter first n line:"))
	m=int(input("Enter last m line: "))
	data=f1.readline()
	for i in data[:n]:
		print(i,end ='')
	for i in data[-m:]:
		print(i,end ='')
  
n = ('C:/SAFU MASTER/sem4/pyy.txt')
with open (n) as f1:
    data = f1.read().split()
    longestword = len(max(data,key=len))
    result=[i for i in data if len(i) == longestword]
    print("The longestword is:",result)
