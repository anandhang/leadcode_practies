def palindromenumber():
    x = -121
    strightnum = str(x)
    reversenum = str(x)[::-1]
    if strightnum == reversenum:
        return True
    else:
        return False
result1 = palindromenumber()
print(result1)