from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = dict(Counter(ransomNote))

        mc = dict(Counter(magazine))

        for r in rc:
            if rc[r] > mc.get(r,0):
                return False

        return True
