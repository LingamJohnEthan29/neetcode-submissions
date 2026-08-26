class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1,1 
        res = max(nums)
        for i in nums:
            if i == 0:
                currMax, currMin = 0,0
            tmp = currMax*i
            currMax = max(currMax*i, currMin*i, i)
            currMin = min(tmp, currMin*i, i)
            res = max(res,currMax)
        return res
        