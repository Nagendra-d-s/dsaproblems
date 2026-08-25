class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right=0,len(height)-1
        leftmax=rightmax=0
        water=0
        while left<right:
            if height[left]<height[right]:
                leftmax=max(leftmax,height[left])
                water+=leftmax-height[left]
                left+=1
            else:
                rightmax=max(rightmax,height[right])
                water+=rightmax-height[right]
                right-=1
        return water