class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            # print(i)
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if len(stack)>0:
                    if stack[-1]=='{' and i=='}':
                        stack.pop()
                    elif stack[-1]=='(' and i==')':
                        stack.pop()
                    elif stack[-1]=='[' and i==']':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            # print(stack)
        return True if len(stack)==0 else False        