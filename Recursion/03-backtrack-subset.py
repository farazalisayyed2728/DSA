def subsets(arr):
    result = []

    def backtrack(index, current):
        # current subset ko result me add karo
        result.append(current[:])

        # har element ko choose karne ka chance
        for i in range(index, len(arr)):

            # Choose
            current.append(arr[i])

            # Explore
            backtrack(i + 1, current)

            # Undo / Backtrack
            current.pop()

    backtrack(0, [])

    return result


arr = [1, 2, 3]

print(subsets(arr))