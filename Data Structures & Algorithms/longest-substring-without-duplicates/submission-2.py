class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # add string to window until window in valid, increase right pointer (expand)
        # remove left from window until string is valid (shrink)
        # record max string at end as this is longest
        left, longest, window=0,0,set()
        for right in range(len(s)):
            if s[right] in window:
                while s[right] in window:
                    window.remove(s[left])
                    left+=1
            window.add(s[right])
            longest=max(longest, right-left+1)
        return longest
        