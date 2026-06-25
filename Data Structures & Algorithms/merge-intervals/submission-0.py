class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        ints = sorted(intervals,key=lambda x:x[0])
        res.append(ints[0])
        if len(ints) == 1:
            return res
        for i in range(1,len(ints)):
            res_int = res[-1]
            comp_int = ints[i]
            if res_int[1] < comp_int[0]:
                res.append(comp_int)
            else:
                res.pop()
                res.append([min(res_int[0],comp_int[0]),max(res_int[1],comp_int[1])])
        return res

        