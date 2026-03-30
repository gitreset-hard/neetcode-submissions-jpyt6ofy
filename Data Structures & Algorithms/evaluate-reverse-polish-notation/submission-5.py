class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        temp = []
        ans = 0
        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:

                if t == "+":
                    ans = stack.pop() + stack.pop()
                    stack.append(ans)
                if t == "-":
                    ans = -1*stack.pop() + stack.pop()
                    stack.append(ans)
                if t == "*":
                    ans = stack.pop() * stack.pop()
                    stack.append(ans)
                if t== "/":
                    a = stack.pop()
                    b = stack.pop()
                    if a!= 0:
                        stack.append(int(b/a))
                    else:
                        raise ValueError
                
        return stack[0]
        
