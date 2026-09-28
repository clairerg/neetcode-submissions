# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        start = head
        while start and prev:
            start_next = start.next
            prev_next = prev.next

            start.next = prev
            prev.next = start_next
            start = start_next
            prev = prev_next
        
        return None
            

        
            
        