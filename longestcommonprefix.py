class Solution:
    def longestCommonPrefix(self, strs):
        # Check if list is empty
        if not strs:
            return ""

        # Take first string as prefix
        prefix = strs[0]

        # Compare with remaining strings
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                # If prefix becomes empty
                if prefix == "":
                    return ""

        return prefix


# Create object
sol = Solution()

# Number of strings input
n = int(input("Enter number of strings: "))

# Empty list
strs = []

# Take strings input one by one
for i in range(n):
    s = input(f"Enter string {i+1}: ")
    strs.append(s)

# Print result
print("Longest Common Prefix:", sol.longestCommonPrefix(strs))["floe"]