class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        s=[]
        res=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while s and temperatures[s[-1]]<temp:
                a=s.pop()
                res[a]=i-a
            s.append(i)
        return res