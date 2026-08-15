class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimise n using hashmap 
        # step 1: iterate and check target-nums[i] in hashmap else store nums[i]: i
        # step 2: iterate until condition is satisfied
        hashmap_nums={}
        for i in range(len(nums)):
            if target-nums[i] in hashmap_nums:
                return [hashmap_nums[target-nums[i]], i]
            else:
                hashmap_nums[nums[i]]=i
        
                
        