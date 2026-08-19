from collections import defaultdict
class Solution(object):

    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        count=0
        li=defaultdict(list)
        f1=[2,3,4,5]
        f2=[4,5,6,7]
        f3=[6,7,8,9]
        remain=0
        for i in reservedSeats:
            li[i[0]].append(i[1])
        for v in li.values():
            f=[1,1,1]
            for seat in v:
                if seat in f1:
                    f[0]=0
                if seat in f3:
                    f[-1]=0
                if seat in f2:
                    f[1]=0
            if f[0]==1 or f[2]==1:
                f[1]=0
            count+=sum(f)
        remain=(n-len(li))*2
        return count+remain