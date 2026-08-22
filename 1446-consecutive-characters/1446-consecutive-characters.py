class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        count,max_count=0,0
        for right in range(len(s)):
            if s[left]!=s[right]:
                left=right
                count=1
            else:
                count+=1
            max_count=max(max_count,count)
        return max_count