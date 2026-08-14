class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bo"""
        d={}
        for i in range(len(nums)):
            if nums[i] in d and abs(i-d[nums[i]])<=k:
                return True
            d[nums[i]]=i
        return False