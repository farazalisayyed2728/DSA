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
                rem = rum + k

            
            res += f.get(rem, 0)
            # res += f.get(rem, 0)
            

        return res