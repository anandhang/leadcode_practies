def longestCommonPrefix(strs):
    if len(strs) <= 1 and len(strs) > 200:
        return ""
    if len(strs) == 1:
        return strs[0]
    smallword = ""
    for i in range(len(strs)):
        if strs[i].lower() != strs[i] or len(strs[i]) == 0 or len(strs[i]) > 200:
            return ""
    i = 0
    smallword = strs[i]
    while i < len(strs)-1:
        if len(smallword) >= len(strs[i+1]):
            smallword = strs[i+1]
        i = i + 1
    temp = ""
    for i in range(len(smallword)):
        startwithlen = 0
        wirdfirst = smallword[i]
        text = ""
        for j in range(len(strs)):
            text = strs[j][i]
            if text == wirdfirst:
                startwithlen = startwithlen + 1
        if startwithlen == len(strs):
            temp = temp + wirdfirst
        else:
            return temp            
    return temp        

def findsmallWord(strs):
    temp = ""
    for i in range(len(strs)):
        for j in range(len(strs)):
            if len(strs[i]) < len(strs[j]):
                temp = strs[i]
    return temp

result = longestCommonPrefix(["ab", "a"])
print(result)