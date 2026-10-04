class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using seen/modify existing array
        seen=[0]*(len(nums)+1)
        for num in nums:
            if seen[num]<0:
                return num
            seen[num]=-1
        
           
        