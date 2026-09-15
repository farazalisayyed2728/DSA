class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        res =  0
        sum = 0
        f ={}

        f[0] = 1

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k
            
            if rem < 0:
                rem = sum % k

            
            res += f.get(rem, 0)
            f[rem] = f.get(rem , 0 ) +1
            

        return res


nums = [4,5,0,-2,-3,1]
k = 5
solution = Solution()
print(solution.subarraysDivByK(nums, k))