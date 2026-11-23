from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = dict(Counter(s))

        ch = ''

        for k, v in count.items():
            if v == 1:
                ch = k
                return s.index(ch)

        if ch == '':
            return -1

