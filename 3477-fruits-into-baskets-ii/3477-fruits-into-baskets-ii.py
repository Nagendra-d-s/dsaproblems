class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        unplaced=0
        d={}
        for i in fruits:
            unplace=True
            for j in range(len(baskets)):
                if i<=baskets[j] and j not in d:
                    d[j]=i
                    unplace=False
                    break
            if unplace:
                unplaced+=1
        return unplaced