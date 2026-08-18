class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==len(nums):
            return max(nums)
        d={}
        for i in range(len(nums)-k+1):
            for j in range(i,i+k):
                d[nums[j]]=d.get(nums[j],0)+1
        max_ele=-1
        for key,val in d.items():
            if val==1:
                max_ele=max(max_ele,key)
        return max_ele

        