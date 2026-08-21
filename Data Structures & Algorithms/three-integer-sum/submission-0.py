class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # start with 2 sum and extent it to 3 sum
        nums.sort()
        ans_set=set()
        ans=[]
        p1,p2,p3=0,1,len(nums)-1
        while p1<p3:
            p2=p1+1
            while p2<p3:
                temp=nums[p1]+nums[p2]+nums[p3]
                if temp==0:
                    # Wrap the result in tuple() to make it hashable
                    temp_tuple = tuple(sorted((nums[p1], nums[p2], nums[p3])))   
                    if temp_tuple not in ans_set:
                        ans_set.add(temp_tuple)
                        ans.append([nums[p1],nums[p2],nums[p3]])
                    p2+=1
                elif temp>0:
                    p3-=1
                else:
                    p2+=1
            p3=len(nums)-1
            p1+=1
        return [n for n in ans]