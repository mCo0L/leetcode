# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum_between_zeros = 0
        resultHead = None
        currentHead = None
        current = head.next

        while current.next:
            sum_between_zeros += current.val
            if sum_between_zeros and current.next.val == 0:
                node = ListNode(val=sum_between_zeros)
                sum_between_zeros = 0
                if not resultHead:
                    resultHead = node
                    currentHead = node
                else:
                    currentHead.next = node
                    currentHead = currentHead.next
                
            current = current.next

        return resultHead