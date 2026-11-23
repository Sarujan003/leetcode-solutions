def minimumSumSubarray(nums, l, r):
    m = float('inf')
    boo = True
    for i in range(len(nums)):
            for j in range(l,r+1):
                if i+j <= len(nums):
                    s = sum(nums[i:i+j])

                if s > 0 and s < m:
                    m = s
                    
                    if boo:
                        boo = False

    if boo:
        return -1

    return m

    


nums = [1, 2, 3, 4]
l = 2
r = 4

print(minimumSumSubarray(nums, l, r))
