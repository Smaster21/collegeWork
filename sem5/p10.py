def printPattern(s, j):
    n = len(s)
    m = len(j)
    for a in range(0, (n - m)):
        count = 0
        for i in range(m):
            if j[i] == s[a + i]:
                count += 1
        if count == m:
            return a
s = input('Text A: ')
j = input('Text B: ')
print("patterns occurs with shift", printPattern(s, j))