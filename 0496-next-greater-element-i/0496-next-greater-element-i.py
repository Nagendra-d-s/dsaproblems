class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        next_greater={}
        for i in nums2:
            while stack and i>stack[-1]:
                next_greater[stack.pop()]=i
            stack.append(i)
        
        while stack:
            next_greater[stack.pop()]=-1
        return [next_greater[num] for num in nums1] 