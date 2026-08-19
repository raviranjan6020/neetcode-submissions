class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer left and right
        # cond:1 increase left pointer by one if sum(nums[left]+nums[right])<target
        # Cond: 2 Decrease right pointer by one if  sum(nums[left]+nums[right])>target
        #  default cond: 3 Return [left+1, right+1]
        left,right=0,len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1, right+1]
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1
             