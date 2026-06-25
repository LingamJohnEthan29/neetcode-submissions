"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        cnt = 0 
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        start_ptr = 0
        end_ptr = 0
        maxCnt = -1
        if not intervals:
            return 0
        while start_ptr != len(starts) and end_ptr != len(ends):
            if starts[start_ptr] < ends[end_ptr]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
                start_ptr += 1
            else:
                cnt -= 1
                end_ptr += 1
        return maxCnt
        