import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        heap=[]
        for num in d:
            heapq.heappush(heap,(d[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        print(heap)
        return [num for count,num in heap]