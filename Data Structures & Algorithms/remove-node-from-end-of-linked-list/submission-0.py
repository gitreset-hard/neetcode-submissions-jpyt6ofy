class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Reverse the list
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        # 2. Remove the Nth node
        # 'prev' is now the head of our reversed list
        dummy = ListNode(0)
        dummy.next = prev
        last = dummy
        curr = prev
        
        ptr = 1
        while curr and ptr < n:
            last = curr
            curr = curr.next
            ptr += 1
        
        # Skip the Nth node
        if curr:
            last.next = curr.next

        # 3. Reverse it BACK to original order
        prev = None
        curr = dummy.next # dummy.next handles if the old head was deleted
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
        return prev