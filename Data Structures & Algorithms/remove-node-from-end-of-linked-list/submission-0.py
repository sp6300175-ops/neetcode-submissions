# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next 

        dummy.next = head
        temp = dummy
        for i in range(length - n):
            temp = temp.next
        temp.next = temp.next.next
        return dummy.next


        