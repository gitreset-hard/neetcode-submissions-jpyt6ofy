# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # Null 1 -> 2 -> 3 -> Null
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            # for the next iteration
            prev = curr
            curr = nextNode
        
        return prev
