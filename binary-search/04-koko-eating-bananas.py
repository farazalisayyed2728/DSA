class Solution(object):
        
    def fun(self , piles , speed):
        h = 0

        for i in range(len(piles)):
            h += piles[i] // speed

            if piles[i] % speed != 0:
                h += 1

        return h
        
    def minEatingSpeed(self, piles, h):
        
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            guess = low + (high - low) // 2

            hour = self.fun(piles, guess)

            if hour > h:
                low = guess + 1

            else:
                res = guess
                high = guess - 1

        return res

piles = [3,6,7,11]
h = 8
solution = Solution()
print(solution.minEatingSpeed(piles, h))  # Output: 4