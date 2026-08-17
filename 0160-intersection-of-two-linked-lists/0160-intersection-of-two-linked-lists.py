# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        #brute force
        """d={}
        temp=headA
        while temp:
            d[temp]=1
            temp=temp.next
        temp=headB
        while temp:
            if temp in d:
                return temp
            temp=temp.next
        return None"""

        #optimal
        if not headA or not headB:
            return None
        temp1=headA
        temp2=headB
        while temp1 != temp2:
            if temp1 is None:
                temp1=headB
            else:
                temp1=temp1.next
            if temp2 is None:
                temp2=headA
            else:
                temp2=temp2.next
        return temp1