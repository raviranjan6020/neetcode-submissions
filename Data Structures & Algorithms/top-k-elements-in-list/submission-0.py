class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force
        # Store freq of all num along with element[freq, element] in hashmap 
        # Get a array of values of hashmap
        # Then sort it 
        # return last k number
        hashmap_nums={}
        for i in range(len(nums)):
            if nums[i] in hashmap_nums:
                hashmap_nums[nums[i]][0]+=1
            else:
                hashmap_nums[nums[i]]=[1, nums[i]]
        freq=[val for val in hashmap_nums.values()]
        freq.sort()
        topkfreq=[]
        for i in range(len(freq)-1, len(freq)-k-1, -1):
            topkfreq.append(freq[i][1])
        return topkfreq
