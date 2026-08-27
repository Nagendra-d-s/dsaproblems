class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        need={}
        for i in t:
            need[i]=need.get(i,0)+1
        window={}
        have=0
        need_count=len(need)
        left=0
        min_length=float('inf')
        res=[-1,-1]
        for right in range(len(s)):
            ch=s[right]
            window[ch]=window.get(ch,0)+1
            if ch in need and window[ch]==need[ch]:
                have+=1
            while have==need_count:
                if right-left+1<min_length:
                    min_length=right-left+1
                    res=[left,right]
                window[s[left]]-=1
                if s[left] in need and window[s[left]]<need[s[left]]:
                    have-=1
                left+=1
        l,r=res
        return s[l:r+1] if min_length!=float('inf') else ""