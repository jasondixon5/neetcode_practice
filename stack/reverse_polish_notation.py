from operator import (add, floordiv, mul, sub)

"""
Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
"""
def interpret_rpn(tokens):

    # TODO: Problem with this approach is that RPN technically only does the
    #       encountered operation on two numbers at a time and stores that
    #       
    operator_tokens = {
        '+': add,
        '/': floordiv,
        '*': mul,
        '-': sub,
    }

    intermediate_values = []

    for i in range(len(tokens)):

        if tokens[i] not in operator_tokens:
            intermediate_values.append(int(tokens[i]))

        else:

            operand2 = intermediate_values.pop()
            operand1 = intermediate_values.pop()

            operation = operator_tokens.get(tokens[i])
            val = operation(operand1, operand2)

            intermediate_values.append(val)

    return intermediate_values[0]

def interpret_rpn_orig(tokens):
   
    operator_tokens = {
        '+': add,
        '/': floordiv,
        '*': mul,
        '-': sub,
    }

    stack = []

    for char in tokens:
        # If operator, take last two items from stack and operate on them
        if char in operator_tokens:
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            val = operator_tokens[char](operand1, operand2)
            stack.append(val)
        
        else:
            stack.append(int(char))

    return stack[0]

def test_interpret_rpn_plus_mult_sub():
    
    tokens = ["1","2","+","3","*","4","-"]
    expected = 5
    sol = interpret_rpn(tokens)

    assert sol == expected

def test_interpret_rpn_contains_twodigit_number():

    tokens = ["1","20","+","3","*","4","-"]
    expected = 59
    sol = interpret_rpn(tokens)

    assert sol == expected

def test_interpret_rpn_contains_twodigit_neg_number():

    tokens = ["1","-20","+","3","*","4","-"]
    expected = -61
    sol = interpret_rpn(tokens)

    assert sol == expected

