class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap solution
        if len(s) != len(t):
            return False
        string_store_s={}
        for i in s:
            if i in string_store_s:
                string_store_s[i]+=1
            else:
                string_store_s[i]=1
        for j in t:
            if j in string_store_s and  string_store_s[j]>0:
                string_store_s[j]-=1
            else:
                return False
        return True


        