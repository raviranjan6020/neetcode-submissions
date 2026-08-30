class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # r1,m,r2
        r1,r2=0,len(matrix)-1
        while r1<=r2:
            m=r1+(r2-r1)//2
            if matrix[m][0]<=target<=matrix[m][-1]:
                l,r=0,len(matrix[m])-1
                while l<=r:
                    mid=l+(r-l)//2
                    if matrix[m][mid]==target:
                        return True
                    elif target>matrix[m][mid]:
                        l=mid+1
                    else:
                        r=mid-1
                return False
            elif target>matrix[m][-1]:
                r1=m+1
            else:
                r2=m-1
        return False
        