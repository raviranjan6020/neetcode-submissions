class Solution:

    def encode(self, strs: List[str]) -> str:
        # Optimal solution in one pass
        # Encode using len(s)+#+s....
        encoded_str=[]
        for s in strs:
            encoded_str.append(str(len(s)))
            encoded_str.append('#')
            encoded_str.append(s)
        return "".join(encoded_str)


    def decode(self, s: str) -> List[str]:
        # Decode length before #(delimiter) and extract string
        decoded_str,i=[], 0
        while i<len(s):
            j=i
            sz=""
            while s[j] != '#':
                sz+=s[j]
                j+=1
            j+=1
            decoded_str.append(s[j:j+int(sz)])
            i=j+int(sz)
        return decoded_str
