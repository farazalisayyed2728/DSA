class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        
                """
                :type nums: List[int]
                :rtype: int
                """
                i = 0
                best_end = arr[0]
                ans = arr[0]

                for i in range(1, len(arr)):
                    v1 = best_end + arr[i]
                    v2 = arr[i]
                    i += 1
                    best_end = min(v1, v2)
                    ans = min(ans , best_end)

                return ans