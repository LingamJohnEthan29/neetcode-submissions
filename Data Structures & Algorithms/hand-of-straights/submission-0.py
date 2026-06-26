class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hash_map = Counter(hand)
        minHeap = list(hash_map.keys())
        heapq.heapify(minHeap)
        #You can also use a TreeMap to remove middle count == 0 in minHeap 
        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in hash_map:
                    return False
                hash_map[i] -= 1
                if hash_map[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True

        