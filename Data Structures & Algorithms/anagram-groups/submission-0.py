class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute force
        # sort the strings to get a unique key 
        # Use 'unique key' as a key in hashmap to store all anagram
        # store all value as array
        # Return all values as a array of array
        hashmap_strs={}
        for word in strs:
            temp="".join(sorted(word))
            if temp in hashmap_strs:
                hashmap_strs[temp].append(word)
            else:
                hashmap_strs[temp]=[word]
        return [val for val in hashmap_strs.values()]