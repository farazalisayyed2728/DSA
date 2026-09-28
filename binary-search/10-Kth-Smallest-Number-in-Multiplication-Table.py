class Solution(object):
    def fun(self ,m ,n ,guess):
        count = 0

        for i in range(1,m + 1):
            count += min(n, guess // i)

        return count 

    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        low = 1
        high = m * n

        res = -1

        while low <= high:
            guess = low + (high - low) // 2
            count = self.fun(m,n,guess)

            if count < k:
                low = guess + 1

            else:
                res = guess
                high = guess - 1

        return res
        