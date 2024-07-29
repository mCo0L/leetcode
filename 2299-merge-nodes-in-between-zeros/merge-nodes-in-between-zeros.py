# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        resultHead = None
        currentHead = None
        current = head.next

        while current.next:
            stack.append(current.val)
            if stack and current.next.val == 0:
                node = ListNode(val=sum(stack))
                stack = []
                if not resultHead:
                    resultHead = node
                    currentHead = node
                else:
                    currentHead.next = node
                    currentHead = currentHead.next
                
            current = current.next

        return resultHead