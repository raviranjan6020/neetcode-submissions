class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute force
        # Create a array with unique numbers and sort it
        # iterate it when diff is greate than 1 then reset and start from there
        # longest
        if len(nums)<2:
            return len(nums)
        nums.sort()
        # print(nums)
        ans,temp=1,1
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1]<2:
                if nums[i]-nums[i-1]==0:
                    continue
                else:
                    temp+=1
            else:
                ans=max(ans,temp)
                temp=1
        return max(ans,temp)