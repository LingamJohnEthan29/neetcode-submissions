# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0 
        ptr = head
        while ptr:
            N += 1
            ptr = ptr.next
        pos = N-n
        position = 0
        if pos == 0:
            return head.next
        ptr1 = head
        while ptr1 and position+1 != pos:
            position += 1
            ptr1 = ptr1.next
        if ptr1.next.next:
            ptr1.next = ptr1.next.next
        else:
            ptr1.next = None
        return head