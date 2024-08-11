from collections import Counter, defaultdict

"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

# Anagram means using all characters of str s, can create str t (all same chars and same quantity of chars)
inputs = {
    ("anagram", "nagaram"): True,
    ("rat", "car"): False,
    ("loony", "yooln"): True,
}

def hashmap_solution(str1: str, str2: str) -> bool:

    """
    Time: O(str1 len + str2 len)
    Space: Same
    """
    
    # Verify strs are same length
    if len(str1) != len(str2):
        return False
    
    # Create hashmaps of chars in each str
    hashmap_1 = defaultdict(int)
    hashmap_2 = defaultdict(int)

    for c in str1:
        hashmap_1[c] += 1
    for c in str2:
        hashmap_2[c] +=1

    """
    Alternative to default dict approach
    hashmap_1, hashmap_2 = {}, {}
    for i in range(len(str1)):
        hashmap_1[str1[i]] = i + hashmap_1.get(str1[i], 0)
        hashmap_2[str2[i]] = i + hashmap_2.get(str2[i], 0)
    """

    # Check that hashmap contents are identical
    for c, cnt in hashmap_1.items():
        if hashmap_2.get(c, None) is None or hashmap_2.get(c, None) != cnt:
            return False
    """
    Alternative:
    for c in hashmap_1:
        if hashmap_1[c] != hashmap_2.get(c, 0):
        return False
    """
    
    return True

def test_hashmap_solution() -> None:

    for input, expected in inputs.items():
        
        str1, str2 = input
        sol = hashmap_solution(str1, str2)
        
        try:
            assert sol == expected
        except AssertionError:
            print(f"Test failed on input {input}\nExpected: {expected}\nReceived: {sol}")
            raise AssertionError

def counter_solution(str1: str, str2: str) -> bool:
    return Counter(str1) == Counter(str2)

def test_counter_solution() -> None:

    for input, expected in inputs.items():

        str1, str2 = input
        sol = counter_solution(str1, str2)
        
        try:
            assert sol == expected
        except AssertionError:
            print(f"Test failed on input {input}\nExpected: {expected}\nReceived: {sol}")
            raise AssertionError

def sorted_solution(str1: str, str2: str) -> bool:
    """
    Time: O(nlogn) 
    Space: O(1) -- if don't count any extra space for sorting
    """
    return sorted(str1) == sorted(str2)

def test_sorted_solution() -> None:

    for input, expected in inputs.items():

        str1, str2 = input
        sol = sorted_solution(str1, str2)
        
        try:
            assert sol == expected
        except AssertionError:
            print(f"Test failed on input {input}\nExpected: {expected}\nReceived: {sol}")
            raise AssertionError



