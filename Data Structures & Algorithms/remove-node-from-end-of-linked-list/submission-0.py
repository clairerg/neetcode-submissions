# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        start = head
        while start:
            length += 1
            start = start.next
        
        count = 0
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy

        new_n = length - n
        while curr:
            if count == new_n:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next   
            count += 1
        
        return dummy.next
        