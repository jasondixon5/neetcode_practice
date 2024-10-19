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

	def backtrack(count_open, count_closed):
	
		if count_open == count_closed == n:
			
			result.append("".join(stack))
			return

		if count_open < n:
			stack.append("(")
			backtrack(count_open + 1, count_closed)
			stack.pop()

		if count_closed < count_open:
			stack.append(")")
			backtrack(count_open, count_closed + 1)
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

