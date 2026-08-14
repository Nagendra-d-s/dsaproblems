class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        left=0
        d=defaultdict()
        for right in range(len(s)):
            d[s[right]]=d.get(s[right],0)+1
            while d[s[right]]>2:
                d[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len