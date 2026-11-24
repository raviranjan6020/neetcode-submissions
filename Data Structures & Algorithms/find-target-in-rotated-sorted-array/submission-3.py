class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: find pivot
        l,r = 0,len(nums)-1 
        while l < r:
            m = l + (r-l) // 2
            if nums[m] > nums[r]:
                l=m+1
            else:
                r=m
        pivot=l

        # step 2: check in which part target is
        if pivot>0 and nums[0]<= target <= nums[pivot-1]:
            # search for target in this
            l, r = 0, pivot-1
        else:
            l, r = pivot, len(nums)-1

        # Step 3: search in this part
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1


            
            
                  