class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
            nums.sort()
            output = []

            for i in range(len(nums)-2):
                if i!=0 and nums[i] == nums[i-1]:
                    continue

                j = i + 1
                k = len(nums) -1

                while(j<k):

                    summation = nums[i] + nums[j] + nums[k]
                    if summation == 0:
                        output.append([nums[i] , nums[j] , nums[k]])

                        while j<len(nums) -1 and nums[j] == nums[j+1]:
                            j += 1

                        j += 1

                    elif summation < 0:
                        while j<len(nums) -1 and nums[j] == nums[j+1]:
                            j += 1

                        j += 1

                    else:
                        while k>2 and nums[k] == nums[k-1]:
                            k -= 1

                        k -= 1


            return output