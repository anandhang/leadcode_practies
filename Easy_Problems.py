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
    
#result = addtwo()
#print(result)

def palindromenumber():
    x = -121
    strightnum = str(x)
    reversenum = str(x)[::-1]
    if strightnum == reversenum:
        return True
    else:
        return False
#result1 = palindromenumber()
#print(result1)
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        strnum = str(s)
        count = 0
        resdic = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
        a = 0
        for n in strnum[::-1]:
            b = resdic.get(n) 
            a = int(a) + int(b)
        return a
'''
'''
def roman(s):
    resdic = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
    for i in range(len(s)):


        n = ""  
        i = i + r      
        if i >= (len(s)):
            break
        if s[i] == "C" and i + 1 < (len(s)):
            if s[i+1] == "M":
                n = "CM"
                r = r + 1
        elif s[i] == "X" and i + 1 < (len(s)):
            if s[i+1] == "C":
                n = "XC"
                r = r + 1  
        elif s[i] == "I" and i + 1 < (len(s)):
            if s[i+1] == "V":
                n = "IV"
                r = r + 1  
            elif s[i+1] == "X":
                    n = "IX"
                    r = r + 1
        if n == "":
            n = s[i]
        b = resdic.get(n) 
        a = int(a) + int(b) 
    return a
result = roman("IX")#MCMXCIV#LVIII
print(result)
'''
'''
def findroman(s : str):
    resdic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100,  "D" : 500, "M" : 1000}
    t = 0
    next = 0
    while next < len(s):
        if next + 1 < len(s) and resdic[s[next]] < resdic[s[next+1]]:
            t = t + int(resdic[s[next+1]]) - int(resdic[s[next]])
            next = next + 2
        else:
            t = t + int(resdic[s[next]])
            next = next + 1        
    return t
result = findroman("MCMXCIV")#MCMXCIV#LVIII
print(result)
'''

'''
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
'''

def useStack(s : str):
    if s == "":
        return False
    if len(s) == 1 or len(s) > 10000:
        return False
    stack = []   
    for i in range(len(s)):
        if s[i] in "({[":
            stack.append(s[i])
        elif s[i] in ")}]" and len(stack) > 0:
            if s[i] == ")" and stack[-1] in "(":                 
                stack.pop()
            elif s[i] == "]" and stack[-1] in "[": 
                stack.pop()
            elif s[i] == "}" and stack[-1] in "{": 
                stack.pop()
            else:
                return False
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False
    
result = useStack("(])")
print(result)