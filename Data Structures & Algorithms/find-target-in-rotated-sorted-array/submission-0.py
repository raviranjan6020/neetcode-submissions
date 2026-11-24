class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # brute force is single iteration and if not then return -1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
        