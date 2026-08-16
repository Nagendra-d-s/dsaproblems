# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        temp=dummy
        curr=head
        while curr:
            if curr.val==val:
                curr=curr.next
            else:
                temp.next=curr
                curr=curr.next
                temp=temp.next
        temp.next=None
        return dummy.next
                
