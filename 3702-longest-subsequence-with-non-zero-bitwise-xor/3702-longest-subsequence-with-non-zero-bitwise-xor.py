class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        temp=0
        has_zero=False
        for i in range(len(nums)):
            temp^=nums[i]
            if nums[i]!=0:
                has_zero=True
        if temp:
            return n
        if has_zero:
            return n-1
        return 0