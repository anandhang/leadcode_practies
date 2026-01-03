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

'''
def useStack(self, s):
    """
    :type s: str
    :rtype: bool
    """
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
'''