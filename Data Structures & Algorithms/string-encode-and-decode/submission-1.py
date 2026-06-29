class Solution:

    def encode(self, strs: List[str]) -> str:
        # Hello World -> 5#Hello5#World
        temp = []
        for s in strs:
            str_len = len(s)
            temp.append(f"{str_len}#{s}")
        
        print(temp)
        return "".join(temp)


    def decode(self, s: str) -> List[str]:
        decoded_str = []

        right = 0
        while right < len(s):

            # find delimeter: #

            start = right
            while s[right] != "#":
                right += 1

            num = int(s[start:right])
            
            # extract next num chars after delimeter
            start = right + 1
            right = start + num
            # extract word
            decoded_str.append(s[start:right])

        
        return decoded_str


            
            


