class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq

        n = len(stones)
        h = []

        for stone in stones:
            heapq.heappush(h, -stone)

        while len(h) > 1:

            x = -heapq.heappop(h)
            y = -heapq.heappop(h)

            if x != y:
                heapq.heappush(h , -(x - y))

        if len(h) == 1:
            return -h[0]

        return 0
stones = [2,7,4,1,8,1]
solution = Solution()
print(solution.lastStoneWeight(stones))