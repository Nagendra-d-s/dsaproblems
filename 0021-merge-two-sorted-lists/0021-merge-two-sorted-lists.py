# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3=ListNode(0)
        temp3=list3
        while list1 and list2:
            if list1.val<=list2.val:
                temp3.next=list1
                list1=list1.next
            else:
                temp3.next=list2
                list2=list2.next
            temp3=temp3.next
        if list1:
            temp3.next=list1
        else:
            temp3.next=list2
        return list3.next
