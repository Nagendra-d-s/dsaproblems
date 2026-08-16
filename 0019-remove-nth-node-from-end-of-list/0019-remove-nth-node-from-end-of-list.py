# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count=0
        k=0
        temp=head
        dummy=ListNode(0)
        temp2=dummy
        while temp:
            temp=temp.next
            k+=1
        temp=head
        while count<=k-n-1:
            temp2.next=temp
            temp=temp.next
            temp2=temp2.next
            count+=1
        temp2.next=temp.next
        return dummy.next