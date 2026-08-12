class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list has 0 or 1 node, no swap needed
        if not head or not head.next:
            return head
        
        # Nodes to be swapped
        first = head
        second = head.next
        
        # Swapping logic
        first.next = self.swapPairs(second.next)
        second.next = first
        
        # second becomes the new head of this sublist
        return second