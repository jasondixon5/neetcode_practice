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

def longest_consecutive_seq_set_approach(nums):
    # Initialize a set based on input arr for efficient checking
    nums_set = set(nums)
    longest_seq = 0

    # For each elem of input array, check if it's start of a sequence
    for n in nums:
        # If start of a seq, calc len of that seq
        # Start identified by having no num to its left on hypoth num line
        if (n -1) not in nums_set:
            length = 0 # Initialize length of this seq
            while (n + length) in nums_set:
                length += 1
            longest_seq = max(length, longest_seq)

    return longest_seq

def test_consecutive_seq_set_approach_no_repeated_nums():
   
   nums = [100,4,200,1,3,2]
   expected = 4
   
   assert expected == longest_consecutive_seq_set_approach(nums)

def test_consecutive_seq_set_approach_repeated_nums():
    
    nums = [0,3,7,2,5,8,4,6,0,1]
    expected = 9
 
    assert expected == longest_consecutive_seq_set_approach(nums)
