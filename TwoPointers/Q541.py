class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s,start,end):
            left = start
            right = end - 1

            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            return s

        
        s = list(s)
        i = 0

        # if k > len(s):
        #     reverse(s,0,len(s))
        #     return "".join(s)
            
        while i < len(s):
            if k > len(s) - i:
                reverse(s,i,len(s))

            elif i+k-1 < len(s):
                reverse(s,i,i+k)

            i = i + 2*k

        return "".join(s)
