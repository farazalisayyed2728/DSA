class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        import heapq
        heap = []
        
        for i in range(len(arr)):
            heapq.heappush(heap, arr[i])
            
        for i in range(k - 1):
            heapq.heappop(heap)
    
        return heapq.heappop(heap)      
