# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        current = head

        while current:
            end = current  
            sum = 0
            while end.val != 0:
                sum += end.val
                end = end.next
            current.val = sum  
            current.next = end.next  
            current = current.next 
        return head