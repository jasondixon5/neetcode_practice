import pytest

"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in 
the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

def hash_set_solution(arr):

    seen = set()

    for i in range(len(arr)):
        if arr[i] in seen:
            return True
        else:
            seen.add(arr[i])
    return False

def test_hash_set_solution():

    inputs = {
    tuple([1,2,3,1]): True,
    tuple([1,2,3,4]): False,
    tuple([1,1,1,3,3,4,3,2,4,2]): True, 
    }

    for input, expected in inputs.items():
        
        sol = hash_set_solution(input)
        assert sol == expected
        