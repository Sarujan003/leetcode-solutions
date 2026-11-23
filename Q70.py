class Solution:
    def climbStairs(self, n: int) -> int:
        output = [1,2]
        n = n -1
        
        if n < 2:
            return output[n]

        for i in range(2,n+1):
            output.append(output[i-2] + output[i-1])

        return output[n]
