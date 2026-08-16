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
        # print(("".join(encoded_string)+"".join(strs)))
        return ("".join(encoded_string)+"".join(strs))


    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        # Extract len of each stings
        strs_len=[]
        i=0
        temp=""
        while i<len(s):
            if s[i]=="#":
                i+=1
                break
            if s[i]==',':
                i+=1
                strs_len.append(int(temp))
                temp=""
                continue
            temp+=s[i]
            i+=1
        
        # Extract strings
        decoded_string=[]
        j=0
        while j<len(strs_len):
            temp=s[i:i+strs_len[j]]
            decoded_string.append(temp)
            i+=strs_len[j]
            j+=1
        return decoded_string            