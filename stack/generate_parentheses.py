"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed
parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""

def backtrack(open_count, closed_count, n, stack, result):

    if open_count == closed_count == n:
        result.append("".join(stack))
        return

    if open_count < n:
        stack.append("(")
        backtrack(open_count + 1, closed_count, n, stack, result)
        stack.pop()

    if closed_count < open_count:
        stack.append(")")
        backtrack(open_count, closed_count + 1, n, stack, result)
        stack.pop()

def generate_parentheses(n):

    stack = []
    result = []

    backtrack(0, 0, n, stack, result)

    return result

def test_generate_parentheses_n3():

	n = 3
	expected = ["((()))","(()())","(())()","()(())","()()()"]
	solution = generate_parentheses(n)

	assert sorted(solution) == sorted(expected)

def test_generate_parentheses_n1():

	n = 1
	expected = ["()"]
	solution = generate_parentheses(n)

	assert sorted(solution) == sorted(expected)
