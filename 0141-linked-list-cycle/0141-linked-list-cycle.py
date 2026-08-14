# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """visited=set()
        current=head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current=current.next
        return False"""
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False