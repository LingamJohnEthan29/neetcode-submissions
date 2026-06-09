class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_dict = dict(zip(position,speed))
        pos = sorted(position, reverse=True)
        stk = []
        fleet = 0
        for i in pos:
            if stk ==[]:
                time = (target - i) / car_dict[i]
                stk.append((i,time))
            else:
                time = (target - i) / car_dict[i]
                if time > stk[-1][1]:
                    stk.append((i,time))
        return len(stk)
