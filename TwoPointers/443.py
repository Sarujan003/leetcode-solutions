class Solution:
    def compress(self, chars: list[str]) -> int:
        j = 0
        i = 0


        # if len(chars) == 1:
        #     return

        
        while i < len(chars):
            count = 0
            if i+1<len(chars):
                if chars[i] == chars[i+1]:
                    chars[j] = chars[i]
                    j+=1
                    duplicate = chars[i]

                    while i<len(chars) and chars[i] == duplicate:
                        i += 1
                        count += 1

                    if count > 1:
                        for k in str(count):
                            chars[j] = k
                            j += 1

                else:
                    chars[j] = chars[i]
                    j += 1
                    i += 1

            else:
                chars[j] = chars[i]
                i += 1
                j += 1


        
        # print(chars[:j])


        return j

