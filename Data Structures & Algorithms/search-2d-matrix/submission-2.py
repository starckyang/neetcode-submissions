class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)*len(matrix[0])-1
        while l<=r:
            m=(l+r)//2
            row=m//len(matrix[0])
            col=m%len(matrix[0])
            cur_num=matrix[row][col]
            if cur_num==target:
                return True
            elif cur_num<target:
                l=m+1
            else:
                r=m-1
        return False
