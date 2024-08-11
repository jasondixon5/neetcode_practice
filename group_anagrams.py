"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

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

inputs = {

    tuple(["eat","tea","tan","ate","nat","bat"]): [
        ["bat"],["nat","tan"],["ate","eat","tea"]],

    tuple([""]): [[""]],

    tuple(["a"]): [["a"]],
}

def group_anagrams_sort_approach(strs):

    """
    Sort each string in the input sequence of strings
    Time: nlogn where n is avg length of the input strings * m times wherre m is how many input strings given in input sequence
    Space: O(1) assuming no extra memory for sorting
    """
    pass

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

    for input_str in strs:
        counts = [0] * 26 # a-z
        
        for char in input_str:
            idx_position = ord(char) - ord('a')
            counts[idx_position] += 1

        # Coerce list to tuple to allow use as a key
        counts = tuple(counts)
        
        if result.get(counts) is None: # Could also use default dict
            result[counts] = [input_str] 
        else:
            result[counts].append(input_str)
    
    return result.values()

def test_group_anagrams_char_frequency_approach() -> None:

    """
    WARNING!!! 
    This test will fail due to constraint in order, even when output is correct. 
    Specifically, can sort within each sublist but unsure how to maintain order
    between function output and expected output.

    So look at test failure manually to determine if output matches input.
    """

    for input, expected in inputs.items():

        sol = group_anagrams_char_frequency_approach(input)        
        
        try:
            assert sol == expected
        except AssertionError:
            print(f"Test failed on input {input}\nExpected: {expected}\nReceived: {sol}")
            raise AssertionError
    



