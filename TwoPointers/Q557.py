class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s):
            left = 0
            right = len(s) - 1

            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            return s

        s = [list(lst) for lst in s.split()]

        for lst in s:
            reverse(lst)

        return " ".join(["".join(lst) for lst in s])
            