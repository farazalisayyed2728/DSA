class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        st = []

        for i in range(2 * len(nums)):
            index = i % len(nums)

            while st and nums[st[-1]] < nums[index]:
                res[st.pop()] = nums[index]

            if  i < len(nums):
                st.append(index)

        return res

    