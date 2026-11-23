### Problem 1: Longest Substring Without Repeating Characters

# *(Core Concept: Sliding Window & Hash Set/Map | Time Target: $O(N)$)*

# * **Problem Statement:**
# Given a string `s`, find the length of the **longest substring** without repeating characters.
# * **Examples:**
# * **Input:** `s = "abcabcbb"`
# * **Output:** `3`
# * **Explanation:** The answer is `"abc"`, with the length of 3.
# * **Input:** `s = "pwwkew"`
# * **Output:** `3`
# * **Explanation:** The answer is `"wke"`, with the length of 3. Notice that the answer must be a substring, `"pwke"` is a subsequence and not a substring.


def longestSubString(s):
    i, j = 0, 0

    max = 0
    seen = set()
    while i < len(s) and j < len(s):
        

        if s[j] not in seen:
            seen.add(s[j])
            j += 1

        else:
            i = j = i + 1
            if max < len(seen):
                max = len(seen)

            seen = set()

    return max

print(longestSubString('abcabcbb'))  # Output: 3 ("abc")
print(longestSubString('pwwkew'))  # Output: 3 ("wke")
print(longestSubString('bbbbb'))  # Output: 1 ("b")
