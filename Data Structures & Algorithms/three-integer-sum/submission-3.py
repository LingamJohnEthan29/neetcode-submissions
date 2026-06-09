class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        ans = []
    
        for i in range(len(nums)):
            a = nums_sort[i]
            if  i > 0 and a == nums_sort[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                b = nums_sort[l]
                c = nums_sort[r]
                if a + b + c == 0:
                    ans.append([a,b,c])
                    l += 1
                    while nums_sort[l] == nums_sort[l-1] and l<r:
                        l += 1
                elif a + b + c > 0:
                    r -= 1
                else:
                    l += 1
        return ans