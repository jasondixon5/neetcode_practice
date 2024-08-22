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

# PRACTICE IN WRITING ALGORITHM

def parentheses_are_balanced(s):

    closed_paren_to_open_map = {
        ")": "(",
        "}": "{",
        "]": "[",
    } 

    parens_seen = []

    for char in s:

        # If it's an open paren, add it to stack
        if char not in closed_paren_to_open_map.keys():
            parens_seen.append(char)
        
        # If it's a closed paren, check to see if last paren seen
        # was its open counterpart 
        else:
            counterpart = closed_paren_to_open_map.get(char)
            
            try:
                latest_paren_seen = parens_seen.pop()
                
                if latest_paren_seen != counterpart:
                    return False

            except IndexError:
                return False
   
    # If no violations found, string is balanced 
    return True 

def test_parentheses_are_balanced_balanced_simple_brackets():
    s = "[]"
    expected = True
    solution = parentheses_are_balanced(s)
    assert solution == expected
    
def test_parentheses_are_balanced_balanced_all_three_types():
    s = "([{}])"
    expected = True
    solution = parentheses_are_balanced(s)
    assert solution == expected
 
def test_parentheses_are_balanced_imbalanced():
    s = "[(])" 
    expected = False
    solution = parentheses_are_balanced(s)
    assert solution == expected
 
def test_parentheses_are_balanced_imbalanced_beg_balanced_end():
    s = "{(})[]"
    expected = False 
    solution = parentheses_are_balanced(s)
    assert solution == expected

def test_parentheses_are_balanced_imbalanced_beg():
    s = "}{(})[]"
    expected = False 
    solution = parentheses_are_balanced(s)
    assert solution == expected
