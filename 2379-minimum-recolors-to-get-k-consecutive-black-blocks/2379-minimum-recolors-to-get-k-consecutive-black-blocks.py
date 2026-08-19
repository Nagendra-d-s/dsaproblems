class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_w=101
        white=0
        black=0
        left=0
        for right in range(len(blocks)):
            if blocks[right]=="W":
                white+=1
            if blocks[right]=="B":
                black+=1
            if black==k:
                return 0
            if right-left+1==k:
                min_w=min(min_w,white)
                if blocks[left]=="W":
                    white-=1
                if blocks[left]=="B":
                    black-=1
                left+=1
        return min_w