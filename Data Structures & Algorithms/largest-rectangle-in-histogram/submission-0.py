class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxArea = -1
        for i in range(len(heights)):
            val = heights[i]
            if stk == []:
                stk.append((i,val))
            else:
                if stk[-1][1] > val:
                    prev_ele = stk[-1]
                    while stk and stk[-1][1] > val:
                        area = (i-stk[-1][0])*(stk[-1][1])
                        maxArea = max(maxArea,area)
                        prev_ele = stk[-1]
                        stk.pop()
                    stk.append((prev_ele[0],val))
                else:
                    stk.append((i,val))
        n = len(heights)
        while stk:
            element = stk.pop()
            area = (n-element[0])*(element[1])
            maxArea = max(area, maxArea)
        return maxArea

                        