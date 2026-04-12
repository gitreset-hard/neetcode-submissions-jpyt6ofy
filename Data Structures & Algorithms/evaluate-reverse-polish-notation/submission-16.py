class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = []
        idx = 0

        for idx, val in enumerate(tokens):

            if val not in "+-/*":
                stack.append(int(tokens[idx]))
            else:
                a,b = stack.pop() ,stack.pop()

                if val == "+":
                    stack.append(a+b)

                if val == "-":
                    stack.append(b-a)

                if val == "*":
                    stack.append(a*b)

                if val == "/":
                    stack.append(int(b / a))

        return stack[0]
