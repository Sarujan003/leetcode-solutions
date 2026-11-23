class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)

        if n1 != n2:
            return False

        counter = {}

        for i in s:
            counter[i] = counter.get(i, 0) + 1

        for i in t:
            if counter.get(i,0) <= 0:
                return False

            else:
                counter[i] = counter.get(i,0) - 1

        return True