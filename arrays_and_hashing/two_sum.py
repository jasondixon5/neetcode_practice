
from typing import Iterable

"""
1. Two Sum

Hint
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not 
use the same element twice.

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
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time 
complexity?

"""
def two_sum_hashmap_approach(nums, target):

    idx_map = {}
    output = []
    
    for i in range(len(nums)):
        diff = target - nums[i]

        if idx_map.get(diff) is not None:
            return [i, idx_map.get(diff)]
        else:
            idx_map[nums[i]] = i

def test_two_sum_hashmap_approach():
    
    inputs = {
        # Sort key only for testing
        ((2,7,11,15), 9): sorted([0,1]),
        ((3,2,4), 6): sorted([1,2]),
        ((3,3),6): sorted([0,1]),
    }

    for input, expected in inputs.items():

        nums = input[0]
        target = input[1]
        sol = sorted(two_sum_hashmap_approach(nums, target))
        
        assert sol == expected
