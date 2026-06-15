class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        ans = []
        maxEle = max(nums[l:r])
        ans.append(maxEle)

        while r < len(nums):
            if nums[l] == maxEle:
                maxEle = max(nums[l + 1:r + 1])
            elif nums[r] > maxEle:
                maxEle = nums[r]

            ans.append(maxEle)
            l += 1
            r += 1

        return ans