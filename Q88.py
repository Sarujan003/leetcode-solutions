nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

j = 0
for i in range(len(nums2)):
    if nums1[j] > nums2[i]:
        nums1[j+1:] = nums1[j:-1]
        nums1[j] = nums2[i]


    j += 1

print(nums1)