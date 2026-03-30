from math import inf
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        cur_min = val if not self.stack else min(self.stack[-1][1],val)
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            
    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1]
        # this is not great, is it better to crete another another monotonic stack?
        # that would 2x the memory so i think not. Want O(n)
        
