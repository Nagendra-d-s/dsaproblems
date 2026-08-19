class Solution(object):
    def maxVowels(self, s, k):
        left=0
        count=0
        max_count=0
        for right in range(len(s)):
            if s[right] in "aeiou":
                count+=1
            if right-left+1==k:
                max_count=max(max_count,count)
                if s[left] in "aeiou":
                    count-=1
                left+=1
        return max_count