class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix[0]), len(matrix)
        l, r = 0, (x*y)-1
        while l <= r:
            mid = (l+r)//2
            my, mx = mid // x, mid % x
            if matrix[my][mx] == target:
                return True
            elif matrix[my][mx] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
