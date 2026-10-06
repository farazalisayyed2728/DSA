def solve(path, choices):

    if len(path) == 2:
        print(path)
        return

    for choice in choices:
        path.append(choice)       # 1. Choose

        solve(path, choices)      # 2. Explore

        path.pop()                # 3. Undo = Backtrack