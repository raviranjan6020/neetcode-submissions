class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Optimal solution
        # will create a hashset and iterate only when for sequence whose num-1 doesn't exist
        # save longest and return
        nums_set=set(nums)
        long=0
        for num in nums:
            if num-1 not in nums_set:
                curr=0
                while num in nums_set:
                    curr+=1
                    num+=1
                long=max(long,curr)
        return long