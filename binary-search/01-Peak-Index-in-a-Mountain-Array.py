class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low = 0
        high = len(arr) -1

        while low <= high: 
            guess = low + (high - low) // 2

            if arr[guess] < arr[guess + 1]:
                low = guess + 1

            else:  
                high = guess - 1

        return low



