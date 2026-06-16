# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        ptr1 = head
        ptr2 = prev

        while ptr2:
            tmp1, tmp2 = ptr1.next,ptr2.next
            ptr1.next = ptr2
            ptr2.next = tmp1
            ptr1, ptr2 = tmp1, tmp2

        


        