class Solution:

    def encode(self, strs: List[str]) -> str:
        # Brute force, use string length seperated by comma and a '#' as a delimiter in front of it then ass whole strings by joing e.g. (3,4,3,4,#ramraviaregood).
        if strs == [""]:
            return ""

        strs_len, encoded_string=[], []
        for s in strs:
            strs_len.append(len(s))

        # Encoding
        for l in strs_len:
            encoded_string.append(str(l))
            encoded_string.append(',')
        encoded_string.append('#')
        return ("".join(encoded_string)+"".join(strs))


    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        # Extract len of each stings
        strs_len=[]
        i=0
        while s[i]!='#':
            j=i
            while s[j]!=',':
                j+=1
            strs_len.append(int(s[i:j]))
            i=j+1
        
        # Extract strings
        i+=1
        decoded_string=[]
        for sz in strs_len:
            decoded_string.append(s[i:i+sz])
            i+=sz
        return decoded_string            