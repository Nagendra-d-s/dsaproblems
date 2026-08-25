class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        max_height=0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                value = heights[stack.pop()]
                if stack:
                    width = i-stack[-1]-1
                else:
                    width = i
                max_height = max(max_height,width*value)
            stack.append(i)
        return max_height