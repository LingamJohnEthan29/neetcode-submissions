class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        filtered = []
        a,b,c = target[0],target[1],target[2]
        for i in triplets:
            x, y, z = i[0],i[1],i[2]
            if x > a or y > b or z > c:
                continue
            else:
                filtered.append(i)
        
        flag_x,flag_y,flag_z = False,False,False

        for i in filtered:
            if i[0] == a:
                flag_x = True
            if i[1] == b:
                flag_y = True
            if i[2] == c:
                flag_z = True
        res = (flag_x and flag_y and flag_z)

        return res

        