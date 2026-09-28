class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # store frequency of all string in a window
        # expand until window is valid(total-max(freq.values)<=k)
        # shring until window is valid(total-max(freq.values)<=k)
        # record longest after each expand
        freq={}
        left,longest=0,0
        majority=0
        total=0

        for right in range(len(s)):
            if  total-majority<=k:
                if s[right] in freq:
                    freq[s[right]]+=1
                else:
                    freq[s[right]]=1
            majority=max(freq.values())
            total=sum(freq.values())
            while total-majority>k:
                freq[s[left]]-=1
                left+=1
                majority=max(freq.values())
                total=sum(freq.values())
            longest=max(longest, right-left+1)
        return longest
            

            
        