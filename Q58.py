class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # count = 0
        # length = 0
        # for ch in s:
        #     if ch == ' ':
        #         count = 0
        #     else:
        #         count = count + 1
            
        #     if count != 0:
        #         length = count
            

        # return length

        length  = 0
        i = len(s) - 1

        # skip the trailling spaces
        while i >= 0 and s[i] == ' ':
            i = i - 1

        while i >= 0  and s[i] != ' ':
            i = i - 1
            length = length + 1

        return length
        