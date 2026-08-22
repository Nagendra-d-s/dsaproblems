class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp=n
        prod=1
        sum=0
        while n>0:
            sum+=n%10
            prod*=n%10
            n//=10
        return temp%(sum+prod)==0