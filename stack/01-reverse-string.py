def reverse_string(s):
    stack = []

    # Push characters into stack
    for ch in s:
        stack.append(ch)

    # Pop characters from stack
    result = ""

    while stack:
        result += stack.pop()

    return result


s = "abc"

print(reverse_string(s))