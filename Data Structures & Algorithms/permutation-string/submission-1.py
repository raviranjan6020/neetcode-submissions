class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute force
        s1="".join(sorted(s1))
        if len(s2)<len(s1):
            return False
        left=0
        for right in range(len(s1), len(s2)):
            temp="".join(sorted(s2[left:right]))
            if s1==temp:
                return True
            left+=1
        
        temp="".join(sorted(s2[left:]))        
        return s1==temp
        