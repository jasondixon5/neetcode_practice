"""
Longest Substring Without Duplicates
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""
def longest_substr_unrepeated_chars(s):

    # keep a count of each character seen
    # or a set of the chars
    # longest_length = 0
    # left_ptr = 0
    # right_ptr = 0

    # while right_ptr < len(s):
        
    #     chars_in_substring = set()
    #     # char_to_check = s[right_ptr]
    #     char_to_check = s[right_ptr]
        
    #     while s[right_ptr] not in chars_in_substring:
        
    #         chars_in_substring.add(s[right_ptr])
    #         local_longest = right_ptr - left_ptr + 1
    #         longest_length = max(longest_length, local_longest)
    #         right_ptr +=1  
        
    #     left_ptr += 1
    #     chars_in_substring.remove(s[left_ptr])
    #     # right_ptr += 1

    # return longest_length

    char_set = set()
    left_ptr = 0
    longest_length = 0

    for right_ptr in range(len(s)):

        while s[right_ptr] in char_set:
            char_set.remove(s[left_ptr])
            left_ptr += 1
        char_set.add(s[right_ptr])
        longest_length = max(longest_length, right_ptr - left_ptr + 1)
    
    return longest_length


def test_longest_substr_unrepeated_chars_substring_len_above_one():
    s = "zxyzxyz"
    expected = 3
    sol = longest_substr_unrepeated_chars(s)
    assert sol == expected

def test_longest_substr_unrepeated_chars_substring_len_one():
    s = "xxxx"
    expected = 1
    sol = longest_substr_unrepeated_chars(s)
    assert sol == expected

        



