class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n * m -1

        while low <= high:
            guess = low + (high -low) // 2
            row = guess // m
            col = guess % m

            if matrix[row][col] == target:
                return True

            if matrix[row][col] < target:
                low = guess + 1

            else:
                high = guess -1

        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
solution = Solution()
print(solution.searchMatrix(matrix, target))