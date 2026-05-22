# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        # start: None -> 0 -> 1 -> 2 -> 3 -> None
        """
        #   1: None <- 0 -> 1 <- 2 <- 3 <- None
        #              prev curr

        """    
        prev = None
        curr = head
        while curr: # 0 ## 1
            next_node = curr.next # 1 ## 2 
            curr.next = prev # -> None ## 0

            prev = curr 
            curr = next_node 
        
        return prev
            

