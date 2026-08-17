# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        d={}
        temp=headA
        while temp:
            d[temp]=1
            temp=temp.next
        temp=headB
        while temp:
            if temp in d:
                return temp
            temp=temp.next
        return None