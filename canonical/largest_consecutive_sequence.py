"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

def setify(seq):

	result = set()

	for elem in seq:
		if elem not in result:
			result.add(elem)

	return result

def longest_consecutive_seq_set_approach(nums):

	nums_check = setify(nums)
	longest = 0

	for i in range(len(nums)):
		temp_length = 0
		if nums[i] - 1 not in nums_check: # Found start of a consec seq
			temp_length = 1
			temp_idx = 1
			while nums[i] + temp_idx in nums_check:
				temp_length += 1
				temp_idx += 1
			longest = max(longest, temp_length)
	
	return longest

def test_consecutive_seq_set_approach_no_repeated_nums():
   
   nums = [100,4,200,1,3,2]
   expected = 4
   
   assert expected == longest_consecutive_seq_set_approach(nums)

def test_consecutive_seq_set_approach_repeated_nums():
    
    nums = [0,3,7,2,5,8,4,6,0,1]
    expected = 9
 
    assert expected == longest_consecutive_seq_set_approach(nums)

def test_consecutive_seq_set_approach_no_sequences_gt_one():
    
    nums = [0,3,7,5,9,23,-2]
    expected = 1 
 
    assert expected == longest_consecutive_seq_set_approach(nums)

def test_consecutive_seq_set_approach_input_empty():
    
    nums = []
    expected = 0 
 
    assert expected == longest_consecutive_seq_set_approach(nums)

