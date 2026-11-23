class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # read = 0
        # for i in range(len(arr)):
        #     if arr[i] == 0:
        #         read += 2

        #     else:
        #         read += 1

        #     if read >= len(arr):
        #         read  = i
        #         break

        # write = len(arr) - 1

        # while read >= 0:
        #     if arr[read] != 0:
        #         arr[write] = arr[read]
        #         read -= 1
        #         write -= 1

        #     else:
        #         arr[write] = 0
        #         read -= 1
        #         write -= 1

        #         if write != 0:
        #             arr[write] = 0
        #             write -=1
        
        zeros = 0
        for i in arr:
            if i == 0:
                zeros += 1

        i = len(arr) - 1

        j = i + zeros

        while i!=j:
            if arr[i] != 0:
                if j < len(arr):
                    arr[j] = arr[i]

                j -= 1
                i -= 1

            else:
                if j < len(arr):
                    arr[j] = 0

                if j - 1 < len(arr):
                    arr[j-1] = 0

                j -= 2
                i -= 1
                    

        
        