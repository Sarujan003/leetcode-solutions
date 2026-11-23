class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        sum_k = 0
        output = [0] * len(code)

        # k > 0
        if k!=0:
            if k > 0:
                for i in range(1, k+1):
                    x = i
                    if x > len(code) - 1:
                        x = x % len(code)

                    sum_k += code[i]

                output[0] = sum_k

                for i in range(1,len(code)):
                    x = i + k
                    if x > len(code) - 1:
                        x = x % len(code)
                    sum_k = sum_k - code[i] + code[x]

                    output[i] = sum_k
            
            else:
                for i in range(k, 0):
                    x = i
                    if x > len(code) - 1:
                        x = x % len(code)

                    sum_k += code[x]

                output[0] = sum_k

                for i in range(k, len(code) + k - 1):
                    # k, 0
                    x = i - k

                    if x > len(code) - 1:
                        x = x % len(code)

                    sum_k = sum_k - code[i] + code[x]

                    output[i-k+1] = sum_k

        return output

