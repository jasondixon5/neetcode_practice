
from typing import Iterable

"""
1. Two Sum

Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
def two_sum_brute_force_approach(nums, target):
    """
    Time: O(n**2)
    Space: O(1)
    """
    pass

# NB: Tried type def
def two_sum_hashmap_approach(nums: Iterable[int], target: int) -> list[int]:
# But got error; E   TypeError: 'type' object is not subscriptable
# Runs fine without running pytest so seems to be specific to that library
# def two_sum_hashmap_approach(nums, target):
    """
    Iterate through the array and map each value to its index as you encounter it
    Note: Do not build the entire hashmap first, because would end up using the same value twice

    Time: O(n)
    Space: O(n)
    """
    num_map = {}
    
    for idx, val in enumerate(nums):

        diff = target - val
        
        if num_map.get(diff) is not None:
            return [num_map.get(diff), idx]
        
        num_map[val] = idx

    # Note: No default return value because guaranteed to have a solution

inputs = {
    ((2,7,11,15), 9): [0,1],
    ((3,2,4), 6): [1,2],
    ((3,3),6): [0,1],
}

def test_two_sum_hashmap_approach():
        
    for input, expected in inputs.items():

        nums = input[0]
        target = input[1]
        sol = two_sum_hashmap_approach(nums, target)
        
        try:
            assert sol == expected

        except AssertionError:
            print(f"Test failed on input {input}\nExpected: {expected}\nReceived: {sol}")
            raise AssertionError

