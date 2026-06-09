class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = 1
        nums.sort()
        while l != len(nums)-1:
            if nums[l]-nums[r] == 0:
                return nums[l]
            l += 1
            r += 1
        