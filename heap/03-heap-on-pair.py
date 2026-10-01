class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        import heapq
        f = {}
        pq = []

        for i in range(len(nums)):
            f[nums[i]] = f.get(nums[i], 0) + 1

        for element, freq in f.items():
            curr = (freq , element)


            if len(pq) < k:
                heapq.heappush(pq ,curr)
                continue

            if curr[0] < pq[0][0]:
                continue

            heapq.heappop(pq)
            heapq.heappush(pq , curr)
        


        res = []

        for freq , element in pq:
            res.append(element)
            
        return res
