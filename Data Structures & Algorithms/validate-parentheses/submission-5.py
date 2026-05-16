class Solution:
    def isValid(self, s: str) -> bool:
        
        valid = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []
        for idx in range(len(s)):
            char = s[idx]
            if char in '([{':
                stack.append(char)
                continue
            
            if stack:
                if stack[-1] == valid[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return stack == []
                