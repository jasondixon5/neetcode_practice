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
            
            try:
                if s[i] == expected_parens.pop():
                    continue
                else:
                    return False
            except IndexError: 
                # Index Error if try to pop from empty list
                # Risky because could also have a bug in i for s[i]
                return False

            
    # If all closing parens were popped, parens were balanced
    if expected_parens:
        return False
    else:
        return True


def is_valid_parentheses_map_closing_to_opening_parens(s):
    # This is the original solution on Neetcode site
    # My solution above was my reimpl from memory and I switched order
    # of dict and what was added to stack

    closing_to_opening_parens_map = {

        '}': '{',
        ']': '[',
        ')': '(',
    }

    expected_openings = []

    for i in range(len(s)):

        # Char is an opening paren
        if s[i] not in closing_to_opening_parens_map.keys(): 
            expected_openings.append(s[i])
        
        # Char is a closing paren
        else:
            
            if not expected_openings:
                return False
            elif expected_openings[-1] != closing_to_opening_parens_map[s[i]]:
                return False
            else:
                expected_openings.pop()

    if not expected_openings: #i.e., all parens were balanced
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

def test_is_valid_parentheses_input_missing_closing_bracket():
    s = "[()"
    expected = False
    solution = is_valid_parentheses(s)
    assert solution == expected

def test_is_valid_parentheses_input_missing_opening_bracket():
    s = "()]"
    expected = False
    solution = is_valid_parentheses(s)
    assert solution == expected

def test_is_valid_parentheses_input_brackets_only_is_valid_orig_appr():
    s = "[]"
    expected = True
    solution = is_valid_parentheses_map_closing_to_opening_parens(s)
    assert solution == expected

def test_is_valid_parentheses_input_brack_brace_paren_is_valid_orig_appr():
    s = "([{}])"
    expected = True
    solution = is_valid_parentheses_map_closing_to_opening_parens(s)
    assert solution == expected

def test_is_valid_parentheses_input_bracket_paren_not_valid_orig_appr():
    s = "[(])"
    expected = False 
    solution = is_valid_parentheses_map_closing_to_opening_parens(s)
    assert solution == expected

def test_is_valid_parentheses_input_missing_closing_bracket_orig_appr():
    s = "[()"
    expected = False
    solution = is_valid_parentheses_map_closing_to_opening_parens(s)
    assert solution == expected

def test_is_valid_parentheses_input_missing_opening_bracket_orig_appr():
    s = "()]"
    expected = False
    solution = is_valid_parentheses_map_closing_to_opening_parens(s)
    assert solution == expected
