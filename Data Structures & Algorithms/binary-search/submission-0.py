def BinarySearch(left, right, arr, target):
    mid = (left+right)//2
    if arr[mid] == target:
        return mid
    else:
        if arr[mid] > target:
            return BinarySearch(left, mid, arr, target)
        else:
            return BinarySearch(mid+1, right, arr, target)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return BinarySearch(0, len(nums)-1, nums, target)