"""
Is Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.

"""

def is_palindrome(s: str) -> bool:

    left_ptr = 0
    right_ptr = len(s) - 1

    def is_alphanum(char):
        char = char.lower()
        
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            return True

        if ord(char) >= ord('0') and ord(char) <= ord('9'):
            return True
        
        return False
    
    while left_ptr < right_ptr:

        while left_ptr < right_ptr and not is_alphanum(s[left_ptr]):
            left_ptr += 1
        while right_ptr > left_ptr and not is_alphanum(s[right_ptr]):
            right_ptr -= 1

        if s[left_ptr].lower() != s[right_ptr].lower():
            return False
    
        left_ptr += 1
        right_ptr -= 1

    return True

def test_is_palindrome_is_true():

   s = "Was it a car or a cat I saw?"
   expected = True

   assert expected == is_palindrome(s)

def test_is_palindrome_is_false():

    s = "tab a cat" 
    expected = False
    
    assert expected == is_palindrome(s)

def test_is_palindrome_true_except_middle():
    s = "at na ta"
    expected = False
    
    assert expected == is_palindrome(s)

def test_is_palindrome_true_except_special_char():

    s = "a man a plan a canal: panama"
    expected = True 
    
    assert expected == is_palindrome(s)


    
            