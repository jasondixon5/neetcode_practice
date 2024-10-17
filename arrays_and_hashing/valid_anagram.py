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
def is_valid_anagram(strs):

    # Anagram means using all characters of str s, can create str t (all same 
    # chars and same quantity of chars)
    
    s1, s2 = strs 

    if len(s1) != len(s2):
        return False

    # Get character counts for each string
    
    s1_letter_counts = {}
    for i in range(len(s1)):
        char = s1[i]
        if char in s1_letter_counts:
            s1_letter_counts[char] += 1
        else:
            s1_letter_counts[char] = 1

    from collections import defaultdict
    s2_letter_counts = defaultdict(int)
    for char in s2:
        s2_letter_counts[char] += 1
    
    # Compare character counts for each string

    for char, char_count in s1_letter_counts.items():
        if char_count != s2_letter_counts.get(char):
            return False

    return True

def test_hashmap_solution() -> None:

    inputs = {
        ("anagram", "nagaram"): True,
        ("rat", "car"): False,
        ("loony", "yooln"): True,
    }

    for input, expected in inputs.items():
        
        sol = is_valid_anagram(input)
        assert sol == expected

 