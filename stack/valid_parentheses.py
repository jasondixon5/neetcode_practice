"""
Validate Parentheses
You are given a string s consisting of the following characters: 
'(', ')', '{', '}', '[' and ']'.

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
    Observe that when a closed parenthesis is encountered in a 'balanced'
    string, it is immediately preceded by its open counterpart.
    Valid: ({})[]
    Invalid: {(})[]
    In the invalid example, '{' is ok and '(' is ok, but to continue to be
    valid, that '(' would have to be followed by its closing counterpart
    ')'. Since it's followed by the previous character's closing counterpart
    (in this case, '}'), the '(' is not 'balanced' and the string is therefore
    invalid.


    use a stack 
    use a hashmap to map each closing parenthesis to its open counterpart
    Time: O(n)
    Space: O(n)

    """ 
    closing_parens = {
        "{": "}",
        "[": "]",
        "(": ")",
    }

    expected_parens = []

    for i in range(len(s)):
        if s[i] in closing_parens:
            expected_parens.append(closing_parens.get(s[i]))
        else:
            if s[i] == expected_parens.pop():
                continue
            else:
                return False
            
    return True




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
