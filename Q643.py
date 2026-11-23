class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = float('-inf')

        # sum of first k elements
        sum_k = 0
        for i in range(k):
            sum_k += nums[i]

        avg = sum_k / k

        if max_avg < avg:
            max_avg = avg

        for i in range(k,len(nums)):
            sum_k = (sum_k - nums[i-k] + nums[i])

            avg = sum_k / k

            if max_avg < avg:
                max_avg = avg


        return max_avg
