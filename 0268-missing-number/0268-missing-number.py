class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total,bi=0,0
        for i in range(len(nums)):
            total^=nums[i]
            bi^=i
        bi^=i+1
        return bi^total