class Solution:
    def isValid(self, s: str) -> bool:
        flag = 0
        stack = []
        
        for x in list(s):
            if x == '(' or x == '{' or x == '[' :
                stack.append(x)
            elif x == ')':
                if len(stack) == 0:
                    return False
                elif stack.pop() == '(':
                    flag = 1
                else:
                    return False
            elif x == ']':
                if len(stack) == 0:
                    return False
                elif stack.pop() == '[':
                    flag = 1
                else:
                    return False
            elif x == '}':
                if len(stack) == 0:
                    return False
                elif stack.pop() == '{':
                    flag = 1
                else:
                    return False
                    
        if flag == 1 and len(stack) == 0:
            return True
        else :
            return False
                
    
    
