"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

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

def sort_solution(nums):
    """
    First sort the input array
    Then only have to iterate once and return if a duplicate is found

    Time: O(nlogn) - O(n) for iter thru list, O(nlogn) for sorting
    Space: O(1) - assuming not counting space used by sorting algo
    """

    pass

def hash_map_solution(nums):

    """
    Allows insertion in O(1) time
    Allows checking if a particular int has been added to hash map already

    Time: O(n) - iter thru list, worst case have to go thru whole list
    Space: O(n) - for hash map, worst case have to store all ints in list
    """
    pass



