def addtwo():
    nums = [3,2,4]
    target = 6
    rnums = []
    i = 0
    for n in nums:
        i = i
        j = 0
        for m in nums:
            j = j
            firstItem = n
            secItem = m
            if firstItem + secItem == target and i != j:
                rnums.append(i)
                rnums.append(j)           
                return rnums
            j=j+1
        i=i+1
    
result = addtwo()
print(result)