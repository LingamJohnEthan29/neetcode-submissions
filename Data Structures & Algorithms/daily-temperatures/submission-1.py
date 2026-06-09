class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0]*(len(temperatures))
        for i in range(len(temperatures)):
            curr = temperatures[i]
            if stk == []:
                stk.append((curr, i))
            else:
                if stk[-1][0] < curr:
                    while stk and stk[-1][0] < curr:
                        element = stk.pop()
                        ans[element[1]] = i-element[1]
                    stk.append((curr,i))
                else:
                    stk.append((curr,i))
        return ans

                



