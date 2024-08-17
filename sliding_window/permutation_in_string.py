"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
def permutation_in_string(s1, s2):
    """
    Look in s2 for a substring of number of characters in s1
    Very similar to looking for an anagram
    NB: Substring matching s1 would be a permutation
    e.g., s1 'ab', s2 'eidbao', both 'ba' and 'ab' would be a permutation
    
    Look at each window in s2 that's the same size as s1

    Given constraint is that s1 and s2 can only contain lowercase English
    letters (a-z).
    """
    if len(s1) > len(s2):
        return False
    
    s1_counts = [0] * 26
    s2_counts = [0] * 26
    matches = 0

    for i in range(len(s1)):
        # s1 counts
        idx_position = ord(s1[i]) - ord('a')
        s1_counts[idx_position] += 1

        # s2 counts
        idx_position = ord(s2[i]) - ord('a')
        s2_counts[idx_position] += 1
    
    for i in range(26):
        if s1_counts[i] == s2_counts[i]:
            matches += 1
    
    left_ptr = 0
    for right_ptr in range(len(s1), len(s2)):
        if matches == 26:
            return True
        
        idx = ord(s2[right_ptr]) - ord('a')
        s2_counts[idx] += 1
        if s1_counts[idx] == s2_counts[idx]:
            matches += 1
        elif s1_counts[idx] + 1 ==  s2_counts[idx]: # were equal but made them unequal with above line
            matches -= 1

        idx = ord(s2[left_ptr]) - ord('a')
        s2_counts[idx] -= 1
        if s1_counts[idx] == s2_counts[idx]:
            matches += 1
        elif s1_counts[idx] - 1 ==  s2_counts[idx]: # were equal but made them unequal with above line
            matches -= 1

        left_ptr += 1

    return matches == 26

def test_permutation_in_string_contains_perm():
    s1 = "ab"
    s2 = "eidbaooo"
    expected = True
    sol = permutation_in_string(s1, s2)
    assert sol == expected

def test_permutation_in_string_does_not_contain_perm():
   s1 = "ab"
   s2 = "eidboaoo"
   expected = False
   sol = permutation_in_string(s1, s2)
   assert sol == expected
