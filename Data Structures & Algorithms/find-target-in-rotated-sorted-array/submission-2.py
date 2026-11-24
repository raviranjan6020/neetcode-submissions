class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # optimise it using binary search

        l,r = 0,len(nums)-1
        # find pivot(which in muminim in array) then search for target in both
        # search for minimum: rule 1, if nums[m]>nums[r] --> l=m+1(as minimum in this half). rule 2, if nums[m]<nums[r] then minimum in first half or at m-->r=m. rule 3, l==r then this is minimum or pivot. 
        while l < r:
            m = l + (r-l) // 2
            if nums[m] > nums[r]:
                # pivot in 2nd part
                l=m+1
            else:
                # pivot in 1st part or at m
                r=m
        # pivot is r=l
        pivot=l
        # check in which part target is

        l,r = 0, len(nums)-1
        if pivot>0 and nums[0]<= target <= nums[pivot-1]:
            # search for target in this
            left, right = 0, pivot-1
            while left<=right:
                mid = left + (right-left)//2
                if nums[mid]==target:
                    return mid
                elif target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
            return -1
        else:
            # search in this
            left, right = pivot, len(nums)-1
            while left<=right:
                mid = left + (right-left)//2
                if nums[mid]==target:
                    return mid
                elif target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
            return -1


            
            
                  