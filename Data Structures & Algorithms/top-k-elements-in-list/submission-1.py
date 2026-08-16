class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Optmisied solution, time O(n) and space O(n) using bucket sort
        # Get the frequency for all elements
        # Do Bucket sort by initializing array with len(array)
        # Store element value at it's freqency position
        # Return tok k frequent
        freq_nums={}
        for n in nums:
            if n in freq_nums:
                freq_nums[n]+=1
            else:
                freq_nums[n]=1 

        bucket_len=len(nums)+1
        bucket=[[] for _ in range(bucket_len)]

        for key,val in freq_nums.items():
            bucket[val].append(key)
        
        topkfreq=[]
        for i in range(len(bucket)-1, 0,-1):
            if bucket[i]!=[]:
                k-=len(bucket[i])
                topkfreq+=bucket[i]
            if k==0:
                break
        return topkfreq

