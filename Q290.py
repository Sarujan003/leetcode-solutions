class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen = {}
        splitted = s.split()
        word_set = set()

        if len(pattern) != len(splitted):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in seen:
                if splitted[i] not in word_set:
                    seen[pattern[i]] = splitted[i]
                    word_set.add(splitted[i])
                
                else:
                    return False

            else:
                if seen[pattern[i]] != splitted[i]:
                    return False

        return True