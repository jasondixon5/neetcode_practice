# Solution to Neetcode 150 set "arrays and hashing"

from re import I


def group_anagrams(strs):

    """
    49. Group Anagrams

    Given an array of strings strs, group the anagrams together. You can return the
    answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different
    word or phrase, typically using all the original letters exactly once.

    Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
    """
    # Create map of pattern to word, where pattern is how many of each
    # lower-case English letter a word has

    patterns = {}

    def create_letter_count(w):
        # Given a word, create map of how many of each letter word has
        templ = [0 for i in range(0,26)]
        for i in range(0, len(w)):
            idx = ord(w[i]) - ord('a') # use ascii vals for idx pos
            templ[idx] += 1

        return templ

    for w in strs:
        templ = create_letter_count(w)
        if tuple(templ) in patterns:
            patterns[tuple(templ)].append(w)
        else:
            patterns[tuple(templ)] = [w]

    return patterns.values()

def is_valid_anagram(s, t):

    """
    242. Valid Anagram

    Given two strings s and t, return true if t is an anagram of s, and false
    otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different
    word or phrase, typically using all the original letters exactly once.


    Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.


    Follow up: What if the inputs contain Unicode characters? How would you adapt
    your solution to such a case?
    """
    # The strs must be same length to possibly be anagrams
    if len(s) != len(t):
       return False

    # Create map of letters and counts for each str
    s_map = {}
    for char in s:
        if char in s_map:
            s_map[char] += 1
        else:
            s_map[char] = 1
    t_map = {}
    for char in t:
        if char in t_map:
            t_map[char] += 1
        else:
            t_map[char] = 1
    for char in s_map:
        if s_map[char] != t_map.get(char):
            return False
    # default
    return True

def two_sum(arr, target):

    """
    1. Two Sum

    Hint
    Given an array of integers nums and an integer target, return indices of the two
    numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not
    use the same element twice.

    You can return the answer in any order.

    Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


    Follow-up: Can you come up with an algorithm that is less than O(n2) time
    complexity?

    """

    val_idx_map = {}

    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in val_idx_map:
            return [val_idx_map[diff], i]
        else:
            val_idx_map[arr[i]] = i

    return []

def contains_duplicates(nums):
    """
    217. Contains Duplicate
    Given an integer array nums, return true if any value appears at least twice in
    the array, and return false if every element is distinct.

    Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    """
    # Could create array or map but going to use set
    nums_seen = set()

    for i in range(len(nums)):
        if nums[i] in nums_seen:
            return True
        else:
            nums_seen.add(nums[i])

    return False

### TESTS ###

def sort_nested_list(list_of_lists):

    new_list_of_lists = []

    for l in list_of_lists:
        sorted_l = sorted(l)
        new_list_of_lists.append(sorted_l)

    return sorted(new_list_of_lists)

def test_group_anagrams_standard():
    strs = ["eat","tea","tan","ate","nat","bat"]
    expected = sort_nested_list([["bat"],["nat","tan"],["ate","eat","tea"]])
    solution = sort_nested_list(group_anagrams(strs))
    assert solution == expected

def test_group_anagrams_empty_str():
   strs = [""]
   expected = sort_nested_list([[""]])
   solution = sort_nested_list(group_anagrams(strs))
   assert solution == expected

def test_group_anagrams_single_item():
   strs = ["a"]
   expected = sort_nested_list([["a"]])
   solution = sort_nested_list(group_anagrams(strs))
   assert solution == expected

def test_valid_anagram():

    s, t = "anagram", "nagaram"
    expected = True
    solution = is_valid_anagram(s, t)
    assert solution == expected

def test_valid_anagram_expect_false():

    s, t = "rat", "car"
    expected = False
    solution = is_valid_anagram(s, t)
    assert solution == expected

def test_two_sum_first_two_elems_match():

    nums = [2,7,11,15]
    target = 9
    expected = sorted([0,1])
    solution = sorted(two_sum(nums, target))
    assert solution == expected

def test_two_sum_later_elems_match():

    nums = [3,2,4]
    target = 6
    expected = sorted([1,2])
    solution = sorted(two_sum(nums, target))
    assert solution == expected

def test_two_sum_only_two_elems():

    nums = [3,3]
    target = 6
    expected = sorted([0,1])
    solution = sorted(two_sum(nums, target))
    assert solution == expected

def test_contains_duplicates_expect_true():
    nums = [1,2,3,1]
    expected = True
    solution = contains_duplicates(nums)
    assert solution == expected

def test_contains_duplicates_expected_false():
    nums = [1,2,3,4]
    expected = False
    solution = contains_duplicates(nums)
    assert solution == expected

def test_contains_duplicates_many_duplicates():

    nums = [1,1,1,3,3,4,3,2,4,2]
    expected = True
    solution = contains_duplicates(nums)
    assert solution == expected
