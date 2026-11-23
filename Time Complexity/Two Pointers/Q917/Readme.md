# Reverse Only Letters

## Intuition

We want to reverse all English/alphabetic characters in a string `s` while keeping non-alphabetic characters (such as hyphens, punctuation, or symbols) in their original positions.

Using a **two-pointer approach** (`left` starting at the beginning and `right` starting at the end) lets us scan toward the center, skip non-letter characters, and swap valid letters in place on a mutable character list before joining them back into a new string.

---

## Approach: Two Pointers with Character List

1. Convert the input string `s` into a list of characters (`s = list(s)`) because Python strings are immutable.
2. Initialize two pointers: `left = 0` and `right = len(s) - 1`.
3. While `left < right`:
   * If both `s[left]` and `s[right]` are alphabetic (`.isalpha()`), swap them and move both pointers inward (`left += 1`, `right -= 1`).
   * Otherwise, advance whichever pointer is currently pointing to a non-alphabetic character (`left += 1` if `not s[left].isalpha()`, and `right -= 1` if `not s[right].isalpha()`).
4. Join the list back into a string (`"".join(s)`) and return it.

---

## Complexity Analysis

### ⚡ Efficiency Summary
* **Current Time Complexity:** $\mathcal{O}(n)$
* **Suggested Time Complexity:** $\mathcal{O}(n)$
* **Verdict:** Optimal and clean linear-time solution.

### 📊 Big-O Complexity Graph (LeetCode Style)

```text
Operations / Time
  ^   O(n!)   O(2^n)   O(n^2)
  |     |       /       /
  |     |      /       /        O(n log n)
  |     |     /       /        /
  |     |    /       /        /      ★ O(n)  <-- Your Solution (Optimal)
  |     |   /       /        /     /
  |     |  /       /        /    /
  |     | /       /        /   /      O(log n)
  |     |/       /        /  /    ---~
  |     /       /        / /  ---~
  |    /       /        //---~        O(1)
  |   /       /       _.-~------------------------
  +------------------------------------------------> Input Size (n)
```

* **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of the string `s`. Converting `s` to a list takes $\mathcal{O}(n)$ time, the `while left < right` loop visits each character at most once (moving `left` right or `right` left on every iteration), and `"".join(s)` takes $\mathcal{O}(n)$ time.
* **Space Complexity:** $\mathcal{O}(n)$ auxiliary space (excluding the returned output string). Creating `list(s)` allocates a list of length $n$ to hold the characters mutably during swapping.

---

## Extra Notes: Does the Original `s` Change?

**No, the original string `s` outside the function will not change.** Here is why:

1. **Strings in Python are immutable:** A `str` object cannot be modified in place.
2. **Local reassignment (`s = list(s)`):** Inside `reverseOnlyLetters`, assigning `s = list(s)` rebinds the local parameter name `s` to a **brand-new `list`** containing the characters of the original string. Swapping elements (`s[left], s[right] = ...`) mutates that local `list`, not the caller's original string.

### Quick Example

```python
original = "a-bC-dEf-ghIj"
sol = Solution()
result = sol.reverseOnlyLetters(original)

print(original)  # "a-bC-dEf-ghIj" (unchanged)
print(result)    # "j-Ih-gfE-dCba" (new reversed string)
```

---

## Python Implementation

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            else:
                if not s[left].isalpha():
                    left += 1

                if not s[right].isalpha():
                    right -= 1

        return "".join(s)
```