class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Brute force
        # use one hashset and start iteration from 1 to len(nums)
        # space O(n) and time O(n)
        numset=set(nums)
        for i in range(1,2^31 -1):
            if i not in numset:
                return i
