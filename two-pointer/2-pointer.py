class solution(object):
    def twosum(self,numbers,target):
        left  = 0
        right = len(numbers) - 1

        while left < right:
            sum  =  numbers[left] + numbers[right]
            if sum > target:
                right -= 1

            elif sum< target:
                right +=1

            else:
                return[left +1, right + 1]


numbers = [2, 7, 11, 15]
solution = solution()
result = solution.twosum(numbers, 9)
print(result)