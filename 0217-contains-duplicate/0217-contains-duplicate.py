class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """ 1)BRUTE FORCE
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False        
        """  #Time:O(n*n) space:O(1)
        """2)Sorting
        nums=sorted(nums)
        for right in range(1,len(nums)):
            if nums[right-1]==nums[right]:
                return True
        return False
        """ #time: O(nlogn) space:O(n)
        
        # 3)USing Hashmap or Hashset
        
        s=set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False #Space:O(n) , Time:O(n)
