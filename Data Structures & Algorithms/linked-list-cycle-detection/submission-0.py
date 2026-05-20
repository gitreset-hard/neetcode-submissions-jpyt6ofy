# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = defaultdict(list)
        while head:
            if len(seen[head.val]) > 1:
                return True
            
            seen[head.val].append(head.next)
            head = head.next
        
        return False