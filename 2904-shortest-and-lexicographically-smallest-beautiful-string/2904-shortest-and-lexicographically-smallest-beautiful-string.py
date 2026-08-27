class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res=""
        left=0
        count=0
        for right in range(len(s)):
            if s[right] == "1":
                count+=1
            while count==k:
                res = self.lexico(res,s[left:right+1])
                if s[left]=="1":
                    count-=1
                left+=1
        return res
    def lexico(self,str1,str2):
        if not str1:
            return str2
        if len(str1)>len(str2):
            return str2
        if len(str1)<len(str2):
            return str1
        return min(str1,str2)
             