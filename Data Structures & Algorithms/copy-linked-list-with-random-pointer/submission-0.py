"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {}
        curr = head
        while curr is not None:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        cur = head
        while cur:
            clone = old_to_new[cur]           # get my clone from the notebook
            clone.next   = old_to_new[cur.next]   if cur.next   else None
            clone.random = old_to_new[cur.random] if cur.random else None
            cur = cur.next

        return old_to_new[head]