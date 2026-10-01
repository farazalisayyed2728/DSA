class Solution(object):
    def distance(self ,point):
        x = point[0]
        y = point[1]

        return x * x + y * y

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        heap = []

        for point in points:
            dist = self.distance(point)
            heapq.heappush(heap , (dist , point))

        ans = []

        for i in range(k ):
            dist , point = heapq.heappop(heap)
            ans.append(point)

        return ans


points = [[3,3],[5,-1],[-2,4]]
k = 2
solution = Solution()
print(solution.kClosest(points, k))