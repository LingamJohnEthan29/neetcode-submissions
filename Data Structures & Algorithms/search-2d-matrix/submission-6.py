def binarySearch(l, r, arr, target):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tot_arr = [num for row in matrix for num in row]
        return binarySearch(0, len(tot_arr)-1,tot_arr,target)