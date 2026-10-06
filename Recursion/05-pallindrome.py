class Solution:
    def isPalindrome(self, s):

        def check(low, high):

            # Base case
            if low >= high:
                return True

            # Characters are different
            if s[low] != s[high]:
                return False

            # Check remaining string
            return check(low + 1, high - 1)

        return check(0, len(s) - 1)
        
s = "abba"
solution = Solution()
print(solution.isPalindrome(s))