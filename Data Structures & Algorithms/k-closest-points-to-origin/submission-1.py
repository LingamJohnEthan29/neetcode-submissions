import heapq,math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        res = []
        for i in points:
            x = i[0]
            y = i[1]
            dist = ((x*x)+(y*y))**0.5
            heapq.heappush(maxHeap,(dist,[x,y]))
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res

