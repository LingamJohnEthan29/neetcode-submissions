class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0 
        ints = sorted(intervals,key=lambda x:x[0])
        stk = []
        stk.append(ints[0])
        prevEnd = ints[0][1]
        if len(ints) == 1:
            return 0
        for i in range(1,len(ints)):
            stk_int = stk[-1]
            int_int = ints[i]

            if stk_int[1] <= int_int[0]:
                stk.append(int_int)
            else:
                res += 1
                stk.pop()
                if stk_int[1] > int_int[1]:
                    stk.append(int_int)
                else:
                    stk.append(stk_int)
        return res


        