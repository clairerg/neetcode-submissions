# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1, list2):
            dummy = ListNode(0)
            prev = dummy
            curr1 = list1
            curr2 = list2

            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    prev.next = curr1
                    curr1 = curr1.next
                    prev = prev.next
                else:
                    prev.next = curr2
                    curr2 = curr2.next
                    prev = prev.next
            
            if curr1:
                prev.next = curr1
            if curr2:
                prev.next = curr2
            
            return dummy.next
        
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i + 1 >= len(lists):
                    merged.append(merge2Lists(lists[i], None))
                else:
                    merged.append(merge2Lists(lists[i], lists[i+1]))
            lists = merged
        
        return lists[0]



    


        