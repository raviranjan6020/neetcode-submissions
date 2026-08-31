class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use 2 pointer
        l,ans=0,0
        longest_s=set()
        for r in range(len(s)):
            if s[r] in longest_s:
                # logic to calculate max and chnage l pointer until s[r] is removed
                while s[r] in longest_s:
                    longest_s.remove(s[l])
                    l+=1
                longest_s.add(s[r])
            else:
                longest_s.add(s[r])
            ans=max(ans, r-l+1)
        return ans        