"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the 
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

def group_anagrams(strs):
   
    anagram_groups = {}

    for s in strs:
        # Get char counts
        char_counts = [0] * 26
        for i in range(len(s)):
            char = s[i]
            # Given constraint of only lowercase English letters,
            # can map char to idx of ascii code
            idx = ord(char) - ord('a')
            char_counts[idx] += 1
        if tuple(char_counts) in anagram_groups:
            anagram_groups[tuple(char_counts)].append(s)
        else:
            anagram_groups[tuple(char_counts)] = [s]

    return anagram_groups.values()

def test_group_anagrams():

    """
    NOTE!!! 
    Special handling (diff to other tests) to ensure order of outputs
    """
    inputs = {

        tuple(["eat","tea","tan","ate","nat","bat"]): [
            ["bat"],["nat","tan"],["ate","eat","tea"]],

        tuple([""]): [[""]],

        tuple(["a"]): [["a"]],
    }

    for input, expected in inputs.items():

        sol = group_anagrams(input)

        sol_sorted = []
        for sublist in sol:
            sol_sorted.append(sorted(sublist))
        sol_sorted = sorted(sol_sorted) # or sol_sorted.sorted()        

        expected_sorted = []
        for sublist in expected:
            expected_sorted.append(sorted(sublist))
        expected_sorted = sorted(expected_sorted)
         
        assert sol_sorted == expected_sorted

def group_anagrams_char_frequency_approach(strs):

    """
    We are given a constraint of a particular char only being in the set of 
    lowercase English letters, i.e., we will only have a-z. 

    Use a hashmap whose key is a list (see note below) representing the 
    pattern (i.e., how many of each char from a to z is in the str) and the 
    value is the strs matching the pattern

    NB: The key is technically a tuple since a list can't be the key in a dict.

    Time: O(m * n) where m is how many input strings given and n is average 
    length of each str (because have to count the number of chars in each str)
    
    """
    result = {}

    # For each str in the input list of strs, map the str to a list whose
    # index is ASCII char code and value is number of instances in str of 
    # that char
    for input in strs:
        # Build array and populate it
        base_arr = [0 for i in range(ord('z')+1)]
        for char in input:
            idx = ord('z') - ord(char)
            base_arr[idx] += 1
        if tuple(base_arr) in result:
            result[tuple(base_arr)].append(input)
        else:
            result[tuple(base_arr)] = [input]

    return result.values()

def test_group_anagrams_char_frequency_approach() -> None:

    """
    NOTE!!! 
    Special handling (diff to other tests) to ensure order of outputs
    """
    inputs = {

        tuple(["eat","tea","tan","ate","nat","bat"]): [
            ["bat"],["nat","tan"],["ate","eat","tea"]],

        tuple([""]): [[""]],

        tuple(["a"]): [["a"]],
    }

    for input, expected in inputs.items():

        sol = group_anagrams_char_frequency_approach(input)

        sol_sorted = []
        for sublist in sol:
            sol_sorted.append(sorted(sublist))
        sol_sorted = sorted(sol_sorted) # or sol_sorted.sorted()        

        expected_sorted = []
        for sublist in expected:
            expected_sorted.append(sorted(sublist))
        expected_sorted = sorted(expected_sorted)

        
        assert sol_sorted == expected_sorted
