"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        stk = []
        ints = sorted(intervals, key=lambda x:x.start)
        res = True
        if not ints:
            return True
        stk.append(ints[0])
        for i in range(1, len(ints)):
            stk_int = stk[-1]
            int_int = ints[i]
            
            if stk_int.end > int_int.start :
                return False
            else:
                stk.pop()
                if stk_int.end > int_int.end:
                    stk.append(stk_int)
                else:
                    stk.append(int_int)
        return res

