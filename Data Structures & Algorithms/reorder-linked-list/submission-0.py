# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        list1 = head
        list2 = slow.next
        slow.next = None

        prev = None
        curr = list2

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        list2 = prev
        p1 = list1
        p2 = list2

        while p1 and p2:
            temp1 = p1.next
            p1.next = p2
            temp2 = p2.next
            p2.next = temp1
            p1 = temp1
            p2 = temp2



