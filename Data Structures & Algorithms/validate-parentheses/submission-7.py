class Solution:
    def isValid(self, s: str) -> bool:
        
        pMap = {"]":"[",
                ")":"(",
                "}":"{"
               }

        stack = []
        for char in s:
            if char in ("({["):
                stack.append(char)
            else:
                if stack and pMap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        
        return stack == []
