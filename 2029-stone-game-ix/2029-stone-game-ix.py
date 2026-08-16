class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        cnt0=cnt1=cnt2=0
        for i in stones:
            if i%3==0:
                cnt0+=1
            elif i%3==1:
                cnt1+=1
            else:
                cnt2+=1
        if cnt0%2==0:
            return cnt1>=1 and cnt2>=1
        return abs(cnt1-cnt2)>2