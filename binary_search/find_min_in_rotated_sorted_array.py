"""
Find Minimum in Rotated Sorted Array
You are given an array of length n which was originally sorted in ascending
order. It has now been rotated between 1 and n times. For example, the array
nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the
array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the
minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that
runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]

Output: 1
Example 2:

Input: nums = [4,5,0,1,2,3]

Output: 0
Example 3:

Input: nums = [4,5,6,7]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""

def find_min(nums):

    left_ptr = 0
    right_ptr = len(nums) - 1
    result = nums[0]

    while left_ptr <= right_ptr:

        mid = (left_ptr + right_ptr) // 2
        result = min(result, nums[mid])

        if nums[mid] > nums[right_ptr]:
            # Search right portion
            left_ptr = mid + 1
        else:
            # Search left portion
            right_ptr = mid - 1

    return min(result, nums[left_ptr])


def test_find_min_two_rotations():
    nums = [3,4,5,6,1,2]
    expected = 1
    solution = find_min(nums)
    assert solution == expected

def test_find_min_four_rotations():
    nums = [4,5,0,1,2,3]
    expected = 0
    solution = find_min(nums)
    assert solution == expected

def test_find_min_no_rotation():
    nums = [4,5,6,7]
    expected = 4
    solution = find_min(nums)
    assert solution == expected
