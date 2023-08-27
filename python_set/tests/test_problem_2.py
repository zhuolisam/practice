from python_set.problem_2 import is_valid_brackets


# Test cases
def test_valid_brackets():
    assert is_valid_brackets("()[]{}") == True
    assert is_valid_brackets("([])") == True
    assert is_valid_brackets("{[]}") == True


def test_invalid_brackets():
    assert is_valid_brackets("(]") == False
    assert is_valid_brackets("([)]") == False
    assert is_valid_brackets("{{[](") == False
    assert is_valid_brackets("{[()]") == False
