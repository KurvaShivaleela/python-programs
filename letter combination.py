class Solution:
    def letterCombinations(self, digits):

        # If input is empty
        if not digits:
            return []

        # Mapping of digits to letters
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        # Backtracking function
        def backtrack(index, current):

            # If combination length equals digits length
            if index == len(digits):
                result.append(current)
                return

            # Get letters for current digit
            letters = phone[digits[index]]

            # Try each letter
            for ch in letters:
                backtrack(index + 1, current + ch)

        # Start recursion
        backtrack(0, "")

        return result


# ---------------- Driver Code ----------------

digits = input("Enter digits (2-9): ")

obj = Solution()

print("Letter Combinations:", obj.letterCombinations(digits))