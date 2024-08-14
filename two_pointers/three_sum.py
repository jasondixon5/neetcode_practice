"""
15. 3Sum
Medium
Topics
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
def three_sum(nums):
    """
    First sort the array
    Then take each elem and run two sum on rest of array
    Time: 
    Space: 
    “"""
    result = []
    nums = sorted(nums)

    for idx, num in enumerate(nums):
        # Avoid re-using same int (input can contain duplicates)
        if idx > 0 and num == nums[idx - 1]:
            continue
        
        # Essentially iterating thru subarray of all elems to right of nums[idx]
        left_ptr = idx + 1
        right_ptr = len(nums) - 1

        while left_ptr < right_ptr:
            three_sum = num + nums[left_ptr] + nums[right_ptr]

            if three_sum == 0:
                result.append([nums[idx], nums[left_ptr], nums[right_ptr]])
                left_ptr += 1
                while nums[left_ptr] == nums[left_ptr - 1] and left_ptr < right_ptr:
                    left_ptr += 1
            
            elif three_sum > 0:
                right_ptr -= 1
            
            else:
                left_ptr += 1

    return result


def compare_list_of_lists(list1, list2):

    assert len(list1) == len(list2)

    if len(list1) == 0:
        assert True

    for idx, subresult in enumerate(list1):
       assert list2[idx] == subresult
        
def test_three_sum_negative_ints():
    nums = [-1,0,1,2,-1,-4]
    expected = [[-1,-1,2],[-1,0,1]]

    sol = three_sum(nums)

    compare_list_of_lists(sol, expected)

def test_three_sum_no_solution():
    nums = [0, 1, 1]
    expected = []

    sol = three_sum(nums)
    compare_list_of_lists(sol, expected)

def test_three_sum_all_zeros():
    nums = [0, 0, 0]
    expected = [[0, 0, 0]]

    sol = three_sum(nums)
    compare_list_of_lists(sol, expected)

def test_three_sum_input_less_than_three():
    nums = [1, -1]
    expected = []

    sol = three_sum(nums)
    assert sol == expected

# def test_three_sum_starting_int_repeated():
#     nums = [-3, 2, 1, 5, -2]
#     expected = [[-3, 5, -2], [-3, 2, 1]]

#     sol = three_sum(nums)
#     compare_list_of_lists(sol, expected)
