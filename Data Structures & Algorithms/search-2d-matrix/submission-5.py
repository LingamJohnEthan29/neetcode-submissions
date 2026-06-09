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
        n = len(matrix)
        for row in matrix:
            if binarySearch(0,len(row)-1,row,target):
                return True
        return False