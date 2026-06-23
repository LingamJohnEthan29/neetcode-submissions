import heapq as hq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums,k
        hq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            hq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        hq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        
