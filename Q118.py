class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        output = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        for i in range(3,numRows+1):
            temp = [1] * i

            for n in range(1,i-1):
                temp[n] = output[-1][n-1] + output[-1][n]

            output.append(temp)



        return output
