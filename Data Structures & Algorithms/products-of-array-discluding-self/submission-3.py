class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        suffix_prod = []
        prefix_prods = 1
        suffix_prods = 1
        N = len(nums)
        for i in range(N):
            prefix_prods *= nums[i]
            prefix_prod.append(prefix_prods)
        for i in range(N-1,-1,-1):
            suffix_prods *= nums[i]
            suffix_prod.append(suffix_prods)
        suffix_prod = suffix_prod[::-1]
        res = []
        for i in range(N):
            left = prefix_prod[i-1] if i > 0 else 1
            right = suffix_prod[i+1] if i < N-1 else 1
            res.append(left * right)
        return res
