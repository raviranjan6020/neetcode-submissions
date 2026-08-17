class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Optimal Solution in one pass
        # Store all 0's position in zero_pos=[]
        # Store pre_prod except 0
        # Set 3 condition: 1. is len(zero_pos)==0: append(pre_prod//nums[i]); condition 2. if len(zero_pos)==1: if nums[i]==0: append(pre_prod) else: append(0) Condition:3 append(0)
        zero_pos, pre_prod=[], 1
        for i in range(len(nums)):
            if nums[i]==0:
                zero_pos.append(i)
            else:
                pre_prod*=nums[i]
        output=[0 for _ in range(len(nums))]
        if len(zero_pos)>1:
            return output
        elif len(zero_pos)==1:
            output[zero_pos[0]]=pre_prod
            return output
        else:
            for i in range(len(nums)):
                output[i]=pre_prod//nums[i]
            return output
            


