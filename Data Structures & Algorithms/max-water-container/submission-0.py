class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force is calculate all posssible combination and return max
        # Optimal solution: use 2 pointer left, right and move min(left, right) pointer and save max result.
        left,right=0,len(heights)-1
        max_water=0
        while left<right:
            temp=(right-left)*min(heights[left],heights[right])
            max_water=max(max_water,temp)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_water
        