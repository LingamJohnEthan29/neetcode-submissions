class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        def dfs(start,path,total):
            if total == target:
                res.append(path.copy())
                return
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                if total + nums[i] > target:
                    break
                path.append(nums[i])
                dfs(i+1,path,total+nums[i])
                path.pop()
        dfs(0,[],0)
        return res
