### Problem 2: Top K Frequent Elements

# *(Core Concept: Hash Map / Frequency Counting & Heap or Bucket Sort | Time Target: $O(N \log K)$ or $O(N)$)*

# * **Problem Statement:**
# Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.
# * **Examples:**
# * **Input:** `nums = [1,1,1,2,2,3], k = 2`
# * **Output:** `[1,2]`
# * **Input:** `nums = [1], k = 1`
# * **Output:** `[1]`

# d = {2: 3, 1: 2, 3: 4}

# print(list(d.values()))

# for k in d.items():
#     print(k)

# print({k:v for k,v in sorted(d.items(), key=lambda x:x[1], reverse=True)})

def TopKFrequentElements(lst):
    count = {}

    for n in lst:
        count[n] = count.get(n,0) + 1

    return list({k:v for k,v in sorted(count.items(), key=lambda x:x[1], reverse=True)}.keys())[:2]

lst = [1,1,1,2,2,3]

print(TopKFrequentElements(lst))



