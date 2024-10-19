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

def generate_parentheses(n):
	
	stack = []
	result = []

	def backtrack(open_paren_n, closed_paren_n):

		if open_paren_n == closed_paren_n == n:
			result.append("".join(stack))
			return

		if open_paren_n < n:
			stack.append("(")
			backtrack(open_paren_n + 1, closed_paren_n)
			stack.pop()

		if closed_paren_n < open_paren_n:
			stack.append(")")
			backtrack(open_paren_n, closed_paren_n + 1)
			stack.pop()

	backtrack(0, 0)
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

