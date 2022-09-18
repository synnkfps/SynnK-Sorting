array = [54, 26, 93,17 ,77 ,31 ,44 ,55 ,20, 13, 23, 17, 83, 23, 91, 98, 23, 11, 6, 4, 8, 9, 10, 23]
array = list(set(array))

def synnk_shorting(L):
    for j in range(len(L)):
        for i in L:
            try:
                if L[L.index(i)+1] > i:
                    x, y = L.index(i), L.index(L[L.index(i)+1])
                    L.insert(x, L[y])
                    L.pop(y+1)
                else:
                    continue   
            except:
                break
    return L

print(synnk_shorting(array))
