def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left] , s[right] = s[right], s[left]

            left += 1
            right -= 1


s = ["h", "e", "l", "l", "o"]

reverseString(s)

print(s)


# A Quick Comparison: Mutable vs. Immutable
# If you tried this with an immutable data type like a string or an integer
# (e.g., passing a string into a function and trying to reassign a character),
# it wouldn't work the same way because strings can't be changed in place. Python would create a brand new object in local memory instead.

# Since lists are mutable, any changes made to them inside a function affect the original object outside as well!