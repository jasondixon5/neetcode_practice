"""
Generate Parentheses
You are given an integer n. Return all well-formed parentheses strings that you 
can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.

Constraints:

1 <= n <= 7
"""
def generate_parentheses(n):

    # Only add open parenthesis if count of open < n
    # Only add closed parenthesis if coount of closed < count of open
    # Generated parentheses str is valid if open == closed == n

    stack = []
    res = []

    # Recursively build generated parentheses str
    def backtrack(open_n, closed_n):
        if open_n == closed_n == n: # base case
            res.append("".join(stack))
            return
        
        if open_n < n:
            stack.append("(")
            backtrack(open_n + 1, closed_n)
            stack.pop()

        if closed_n < open_n:
            stack.append(")")
            backtrack(open_n, closed_n + 1)
            stack.pop()
    
    backtrack(0, 0)
    return res

def test_generate_parentheses_single_pair():

    n = 1
    expected = ["()"]
    sol = generate_parentheses(n)

    assert sol == expected

def test_generate_parentheses_multiple_pairs():

    n = 3
    expected = ["((()))","(()())","(())()","()(())","()()()"]
    sol = generate_parentheses(n)

    assert sol == expected 
