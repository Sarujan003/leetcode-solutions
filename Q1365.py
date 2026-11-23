def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
        l = 0

        output = [len(nums) - 1] * len(nums)

        r = 1

        while l < len(nums) - 1:
            if nums[l] > nums[r]:
                output[r] -= 1

            elif nums[l] < nums[r]:
                output[l] -= 1
            
            else:
                output[r] -= 1
                output[l] -= 1

            r +=1
            if r == len(nums):
                l += 1
                r = l+ 1

        return output
            

nums = [8, 1, 2, 2, 3]
smallerNumbersThanCurrent(nums)