"""
Validate Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
"""
def is_valid_parentheses(s):
   """
   use a stack 
   use a hashmap to map each closing parenthesis to its open counterpart
   Time: O(n)
   Space: O(n)

   """ 
   close_to_open_map = {
      ")": "(",
      "}": "{",
      "]": "[",
   }
    
   stack = []

   for char in s:
       if char in close_to_open_map: #i.e., if char is a closing paren
           
           # Check stack not empty and that last item is the opening
           # paren for this char
           if stack and stack[-1] == close_to_open_map.get(char):
               stack.pop()
           else:
               return False
           
       else:
           stack.append(char)
   
   if not stack:
       return True
   else:
       return False

def test_is_valid_parentheses_input_brackets_only_is_valid():
    s = "[]"
    expected = True
    solution = is_valid_parentheses(s)
    assert solution == expected

def test_is_valid_parentheses_input_brack_brace_paren_is_valid():
    s = "([{}])"
    expected = True
    solution = is_valid_parentheses(s)
    assert solution == expected

def test_is_valid_parentheses_input_bracket_paren_not_valid():
    s = "[(])"
    expected = False 
    solution = is_valid_parentheses(s)
    assert solution == expected
