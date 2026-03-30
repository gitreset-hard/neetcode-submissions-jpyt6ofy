class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""

        encoded = []
        for word in strs:
            encoded.extend( [str(len(word)),"#",word])

        return "".join(encoded)
        
    def decode(self, s: str) -> List[str]:
        if s == "": return []

        decoded = []
        i = 0
        
        while i < len(s):
            # find length
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            
            # extract word of length
            word = s[i:i+length]
            decoded.append(word)
            i += length
        
        return decoded
            
