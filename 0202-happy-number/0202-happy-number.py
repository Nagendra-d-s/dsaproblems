class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()
        curr=str(n)
        if n==1:
            return True
        while curr not in seen:
            seen.add(curr)
            sum=0 
            for i in curr:
                sum+=int(i)**2
            curr=str(sum)
            if sum==1:
                return True
        return False