class Solution(object):
    def isValid(self, p):
        """
        :type s: str
        :rtype: bool
        """
        d={'{':'}','[':']','(':')'}
        s=[]
        for i in p:
            if i in d:
                s.append(i)
            elif len(s)==0 or d[s.pop()]!=i:
                return False
        return not s