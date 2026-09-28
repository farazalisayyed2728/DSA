class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])

        row = n -1
        col = 0

        while row >= 0 and col < m :
            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                row -= 1

            else:
                col += 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
solution = Solution()
print(solution.searchMatrix(matrix, target))
