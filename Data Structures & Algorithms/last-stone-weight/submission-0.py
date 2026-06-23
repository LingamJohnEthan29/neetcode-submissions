import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)

            if stone1 == stone2:
                continue
            else:
                if stone1 < stone2:
                    heapq.heappush(maxHeap, -(stone2-stone1))
                else:
                    heapq.heappush(maxHeap,-(stone1-stone2))
        if maxHeap:
            return -maxHeap[0]
        return 0
