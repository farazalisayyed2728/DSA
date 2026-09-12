class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digit_square_sum(n):
            total = 0
        
            while n > 0:
                d = n % 10
                n = n/10
                total = total + d * d
            return total

        slow = n
        fast = n

        while True:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(digit_square_sum(fast))


            if fast == 1:
                return True


            if slow == fast:
                return False 