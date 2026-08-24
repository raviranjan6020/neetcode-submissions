class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Brute force
        # so use stack and put in stack, stop when you get any expression, pop 2 elements and do operation and add back to stack.
        # do untill all are end and return ans i.e. last element pop
        stack=[]
        for tk in tokens:
            if tk in ['+','-','*','/']:
                # do operation
                a, b= stack.pop(), stack.pop()
                if tk == '+':
                    stack.append(a+b)
                elif tk == '-':
                    stack.append(b-a)
                elif tk == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(float(b)/a))
            else:
                stack.append(int(tk))
        return stack.pop()
        