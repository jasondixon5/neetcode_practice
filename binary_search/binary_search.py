"""
Binary Search
You are given an array of distinct integers nums, sorted in ascending order,
and an integer target.

Implement a function to search for target within nums. If it exists, then
return its index, otherwise, return -1.

Your solution must run in
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
"""
def binary_search(nums, target):

    left_ptr = 0
    right_ptr = len(nums) - 1

    while left_ptr <= right_ptr:

        midpoint = (left_ptr + right_ptr) // 2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] > target:
            # right_ptr -= 1
            right_ptr = midpoint - 1
        else:
            # left_ptr += 1
            left_ptr = midpoint + 1

    return -1

def binary_search_neetcode(nums, target):
    # Two pointer approach

    left_ptr = 0
    right_ptr = len(nums) - 1

    while left_ptr <= right_ptr:

        midpoint = (left_ptr + right_ptr) // 2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] > target:
            right_ptr = midpoint - 1
        else:
            left_ptr = midpoint + 1

    return -1

def binary_search_recursive_not_working(nums, target):
    # TODO: Look further at why this doesn't work
    # Passed all tests except test_binary_search_target_exists_at_end()


    midpoint = len(nums) // 2

    if len(nums) < 2 and nums[midpoint] != target:
        return -1

    if nums[midpoint] == target:
        return midpoint
    elif nums[midpoint] > target:
        return binary_search(nums[0:midpoint], target)
    else:
        return binary_search(nums[midpoint:], target)

    return -1

def test_binary_search_target_exists_near_center():
    nums = [-1,0,2,4,6,8]
    target = 4
    expected = 3
    solution = binary_search(nums, target)

    assert solution == expected

def test_binary_search_target_exists_at_beginning():
    nums = [-1,0,2,4,6,8]
    target = -1
    expected = 0
    solution = binary_search(nums, target)

    assert solution == expected

def test_binary_search_target_exists_at_end():
    nums = [-1,0,2,4,6,8]
    target = 8
    expected = 5
    solution = binary_search(nums, target)

    assert solution == expected

def test_binary_search_target_does_not_exist():
    nums = [-1,0,2,4,6,8]
    target = 3
    expected = -1
    solution = binary_search(nums, target)

    assert solution == expected
