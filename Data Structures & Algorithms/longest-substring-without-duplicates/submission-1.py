class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use 2 pointer
        l,r=0,0
        ans,longest_s=0,set()
        while r<len(s):
            if s[r] in longest_s:
                while s[r] in longest_s:
                    longest_s.remove(s[l])
                    l+=1
            longest_s.add(s[r])
            ans=max(ans,r-l+1)
            r+=1
        return ans
