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

	def backtrack(open_paren_count, closed_paren_count):

		if open_paren_count == closed_paren_count == n:
			result.append("".join(stack))
			return

		if open_paren_count < n:
			stack.append("(")
			backtrack(open_paren_count + 1, closed_paren_count)
			stack.pop()

		if closed_paren_count < open_paren_count:
			stack.append(")")
			backtrack(open_paren_count, closed_paren_count + 1)
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

