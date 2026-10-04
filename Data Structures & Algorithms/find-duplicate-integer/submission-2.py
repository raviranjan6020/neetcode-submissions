class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using modify existing array
        for num in nums:
            idx= abs(num)-1
            if nums[idx]<0:
                return idx+1
            nums[idx]*=(-1)
        
        
           
        