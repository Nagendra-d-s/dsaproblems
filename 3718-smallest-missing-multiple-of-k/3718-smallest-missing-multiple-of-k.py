class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=set(nums)
        for i in range(k,(len(nums)+1)*k,k):
            if i not in s:
                return i
        return i+k