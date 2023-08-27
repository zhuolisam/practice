# Questions:
# Given a string (string brackets) containing just the characters '(', ')', '{', '}', '[' and ']', return a result to determine if the input string is valid. A valid string must adhere to the following rules:
# Determine if the input string is valid. A valid string must adhere to the following rules:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Solution:
# Use a stack to keep track of the opening brackets. Everytime we encounter a closing bracket, we check if the top of stack is the corresponding opening bracket. I have used a recursive approach to solve this problem.

def is_valid_brackets(s) -> bool:
    """_summary_

    Args:
        s (string): String brackets

    Returns:
        bool: is valid brackets
    """

    # mapping of opening and closing brackets
    mapping = {')': '(', '}': '{', ']': '['}

    def helper(stack, remaining):
        if not remaining:
            return not stack
        char, rest = remaining[0], remaining[1:]

        if char in mapping.values():
            return helper(stack + [char], rest)
        elif char in mapping.keys():
            if stack and stack[-1] == mapping[char]:
                return helper(stack[:-1], rest)
            else:
                return False
        else:
            return False

    return helper([], s)
