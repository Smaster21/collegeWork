def Trump_card(c):
    for i in range(1,len(c)):
        key = card[i]
        j = i-1
        
        while j>=0 and key<c[j]:
            c[j+1] = c[j]
            j -= 1
        c[j+1] = key
    return c

card = ['D','W','A','S','E','U','G']
I_sort = Trump_card(card)
print("The Trump card after arranging: ",I_sort)
