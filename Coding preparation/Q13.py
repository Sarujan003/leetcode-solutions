from collections import Counter

k = 4

arr = [1,3,3,4,1,2,4,2,1,3,1]

count = {k:v for k,v in sorted(dict(Counter(arr)).items(),
                                key= lambda x:x[1],
                                reverse=True)
        }

for key,freq in count.items():
    if freq == k:
        print(key)