"""
167. Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

def two_sum(nums, target):
    """
    Note that in output index should be 1-based, not 0-based (problem cnostraint)
    
    Since know array is sorted, if arrive at possibility that exceeds target,
    do not have to continue looking at the next number
    
    Time: O(n)
    Space: O(1)
    """
    left_ptr = 0
    right_ptr = len(nums) - 1

    while left_ptr < right_ptr:

        if nums[left_ptr] + nums[right_ptr] == target:
            return [left_ptr+1, right_ptr+1]
        
        if nums[left_ptr] + nums[right_ptr] > target:
            right_ptr -= 1
        else:
            left_ptr += 1

    # Per problem constraints there should always be a solution
    # but including default return anyway
    return []

def test_two_sum_standard():
    numbers = [2,7,11,15]
    target = 9
    expected = [1,2]

    assert expected == two_sum(numbers, target)

def test_two_sum_negative_numbers_in_input():
    numbers = [-1,0]
    target = -1
    expected = [1,2]

    assert expected == two_sum(numbers, target)
