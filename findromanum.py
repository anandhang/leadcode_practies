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