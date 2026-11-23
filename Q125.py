class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = 0
        left = len(s) - 1

        while right < left:
            if s[right].isalnum() and s[left].isalnum():
                if s[right].lower() == s[left].lower():
                    right += 1
                    left -= 1

                else:
                    return False

            else:
                if not s[right].isalnum():
                    right += 1

                if not s[left].isalnum():
                    left -= 1

        return True