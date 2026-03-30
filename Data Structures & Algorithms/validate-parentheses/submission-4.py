class Solution:
    def isValid(self, s: str) -> bool:

        """
        brute force: " {}[()]"
            - remove matching pairs
            - if len(remaining) != 0: return False    
        
        optimized: use a stack
            push to stack if open
            if closed, it must close the last open (top of stack)
        "([{}])"
        stack: ([{ 

        """
        valid = { "}":"{", ")":"(", "]":"[" }

        stack = []
        for i in range(len(s)):
            if s[i] in valid:
                if stack and stack[-1] != valid[s[i]]: 
                    return False
                elif stack and stack[-1] == valid[s[i]]: 
                    stack.pop()
                elif not stack:
                    return False
            else:
                stack.append(s[i])

        return True if not stack else False