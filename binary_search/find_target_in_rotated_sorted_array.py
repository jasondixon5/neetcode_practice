"""
Find Target in Rotated Sorted Array
You are given an array of length n which was originally sorted in ascending
order. It has now been rotated between 1 and n times. For example, the array
nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of
target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that
runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2], target = 1

Output: 4
Example 2:

Input: nums = [3,5,6,0,1,2], target = 4

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= target <= 1000
"""

def find_target(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            # Determine which area of list to search
            if nums[mid] > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # [3, 4, 5, 0, 1, 2]
            if nums[mid] > nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1

def test_find_target_target_is_second_element():

    nums = [3,4,5,6,1,2]
    target = 1
    expected = 4
    solution = find_target(nums, target)
    assert solution == expected

def test_find_target_target_not_found():

    nums = [3,5,6,0,1,2]
    target = 4
    expected = -1
    solution = find_target(nums, target)
    assert solution == expected
