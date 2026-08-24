class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first=float('-inf')
        second=float('-inf')
        third=float('-inf')

        for i in nums:
            if i==first or i==second or i==third:
                continue
            if i>first:
                third=second
                second=first
                first=i
            elif i>second:
                third=second
                second=i
            elif i>third:
                third=i
        if third==float('-inf'):
            return first
        return third
