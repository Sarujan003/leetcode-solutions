class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        j = 0
        i = 0

        while i < len(typed):
            if name[j] == typed[i]:
                j += 1
                i += 1

                if j > len(name) - 1:
                    j = len(name) - 1
            

            else:
                if i == 0:
                    return False

                if typed[i] == typed[i-1]:
                    i += 1

                else:
                    return False

        return i == len(typed) and j == len(name) - 1 and typed[-1] == name[-1]