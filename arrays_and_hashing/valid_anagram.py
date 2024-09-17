from collections import Counter, defaultdict

"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt 
your solution to such a case?
"""

def hashmap_solution(s, t):

    # Anagram if each str has same chars and same count of those chars

    if len(s) != len(s):
        return False

    s_char_map = {}
    t_char_map = {}

    for char in s:
        if char in s_char_map:
            s_char_map[char] += 1
        else:
            s_char_map[char] = 1

    for char in t:
        if char in t_char_map:
            t_char_map[char] += 1
        else:
            t_char_map[char] = 1

    return s_char_map == t_char_map

def hashmap_solution_not_using_dict_equality(s, t):
    # Alternate solution that does not use Python's dict eq functionality

    if len(s) != len(t):
        return False
    
    s_char_map = {}
    t_char_map = {}

    for char in s:
        if char in s_char_map:
            s_char_map[char] += 1
        else:
            s_char_map[char] = 1

    for char in t:
        if char in t_char_map:
            t_char_map[char] += 1
        else:
            t_char_map[char] = 1

    for char in s_char_map:
        if s_char_map[char] == t_char_map.get(char):
            del t_char_map[char]

    # If dicts equal then second dict should be empty
    return not t_char_map

# Anagram means using all characters of str s, can create str t (all same chars 
# and same quantity of chars)
def test_hashmap_solution() -> None:

    inputs = {
        ("anagram", "nagaram"): True,
        ("rat", "car"): False,
        ("loony", "yooln"): True,
    }

    for input, expected in inputs.items():
        
        str1, str2 = input
        sol = hashmap_solution(str1, str2)
        assert sol == expected

def test_hashmap_solution_not_using_dict_equality() -> None:
    
    inputs = {
        ("anagram", "nagaram"): True,
        ("rat", "car"): False,
        ("loony", "yooln"): True,
    }

    for input, expected in inputs.items():
        
        str1, str2 = input
        sol = hashmap_solution_not_using_dict_equality(str1, str2)
        assert sol == expected
        
def counter_solution(str1: str, str2: str) -> bool:
    """
    Use Python's built-in Counter class to create a dictionary for each string of
    the format {'character': count} and then compare the two dictionaries.
    """
    return Counter(str1) == Counter(str2)

def test_counter_solution() -> None:

    inputs = {
        ("anagram", "nagaram"): True,
        ("rat", "car"): False,
        ("loony", "yooln"): True,
    }

    for input, expected in inputs.items():

        str1, str2 = input
        sol = counter_solution(str1, str2)
        assert sol == expected
        
def sorted_solution(str1: str, str2: str) -> bool:
    """
    Sort the strings. If two strings have the same number of chars in the same
    order they're identical.
    Time: O(nlogn) 
    Space: O(1) -- if don't count any extra space for sorting
    """
    return sorted(str1) == sorted(str2)

def test_sorted_solution() -> None:

    inputs = {
        ("anagram", "nagaram"): True,
        ("rat", "car"): False,
        ("loony", "yooln"): True,
    }

    for input, expected in inputs.items():

        str1, str2 = input
        sol = sorted_solution(str1, str2)
        
        assert sol == expected
  