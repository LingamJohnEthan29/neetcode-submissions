class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0    
        rob3, rob4 = 0,0
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(n-1):
            temp1  = max(rob1 + nums[i], rob2)
            rob1 = rob2 
            rob2 = temp1 
            temp2 = max(rob3 + nums[n-i-1], rob4)
            rob3 = rob4
            rob4 = temp2
        return max(rob2,rob4)

        