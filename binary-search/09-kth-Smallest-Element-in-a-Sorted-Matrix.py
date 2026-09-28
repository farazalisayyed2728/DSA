class Solution(object):
    def fun(self , matrix , n , m , guess):
        row = n -1
        col = 0
        count = 0

        while row >= 0 and col < m :
            if matrix[row][col ] <= guess :
                count = count + row + 1
                col += 1

            else:
                row -= 1

        return count


    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        n = len(matrix)
        m = len(matrix[0])
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        res = -1

        while low <= high :
            guess = low + (high -low) // 2
            ans = self.fun(matrix , n , m ,guess)
            if ans < k :
                low = guess + 1

            else :
                res = guess
                high = guess - 1

        return res


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
solution = Solution()
print(solution.kthSmallest(matrix, k))