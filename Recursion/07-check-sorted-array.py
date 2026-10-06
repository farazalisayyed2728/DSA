class Solution:
    def isSorted(self, arr):
        def check(i):
            # Base case
            if i == len(arr) - 1:
                return True

            # If current element > next element
            if arr[i] > arr[i + 1]:
                return False

            # Check remaining elements
            return check(i + 1)

        return check(0)


arr = [10, 20, 30, 40, 50]
sol = Solution()
print(sol.isSorted(arr))  # Output: True