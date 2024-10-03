
"""
Top K Elements in List
Given an integer array nums and an integer k, return the k most frequent 
elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

"""
    One approach, create pairs (e.g., hashmap) where first elem in pair is
    the int found in the input and the second element is the count of how
    many times that elem appears. Then can sort by the second elem and return
    however many items need to.
    Time: nlogn (for sort)

    Another solution is a max heap. Still will create the pairs of 
    elem->count, but will then store the pairs in heap where key
    would be the # of occurrences. Then pop from heap k times.
    Heapify in python would be O(n) then would pop k times where each
    pop takes O(logn), so time is O(klogn)

    A third solution is possible in time O(n) (linear time) and space O(n)
    This uses bucket sort.
    Noormally bucket sort taught as using an array with the index being the int seen
    and the value is the count.
    Would be linear time if input values were bounded. e.g., if know in advance
    there are only 100 elements can use an array of size 100.
    Also doesn't clearly show where top k elements would be.

    Variation in this approach is to still use an array.
    Index of array will be the count.
    Value of array will be a list of which values have that particular count.

    input: [1, 1, 1, 2, 2, 100]
    idx    val
    0 .   []
    1 .   [100]
    2 .   [2]
    3 .   [1]
    Then start at end of array and go backwards
    """

def top_k_frequent(nums, k):

    # Get counts of each val
    val_counts = {}
    for i in range(len(nums)):
        val = nums[i]
        if val in val_counts:
            val_counts[val] += 1
        else:
            val_counts[val] = 1

    # Convert counts to a list
    count_list = [[] for i in range(len(nums)+1)]
    for val, val_count in val_counts.items():
        count_list[val_count].append(val)

    # Get most frequent elems up to k
    output = []
    for i in range(len(count_list) - 1, -1, -1):
        if count_list[i]:
            output.extend(count_list[i])
            if len(output) >= k:
                return output

def test_top_k_frequent():

    inputs = {
    ((1,2,2,3,3,3), 2): [2,3],
    ((7,7), 1): [7],
    }

    for input, expected in inputs.items():

        nums, k = input

        sol = top_k_frequent(nums, k)
    
    assert sol == expected

def top_k_frequent_elements_bucket_approach(nums, k):

    # Store each unique val in input list and # of occurrences
    freq_counts = {}
    for n in nums:
        freq_counts[n] = freq_counts.get(n, 0) + 1
    
    # Store each elem in sublist at an idx in outer list matching
    # its frequency
    freq_map = [[] for n in range(len(nums) + 1)]
    for val, freq in freq_counts.items():
        freq_map[freq].append(val)

    # Return top k elements
    result = []
    for i in range(len(freq_map) - 1, 1, -1):
        for n in freq_map[i]:
            result.append(n)
        
        if len(result) == k:
            return result
        
def test_top_k_frequent_elements_bucket_approach():

    inputs = {
    ((1,2,2,3,3,3), 2): [2,3],
    ((7,7), 1): [7],
    }

    for input, expected in inputs.items():

        nums, k = input

        sol = top_k_frequent_elements_bucket_approach(nums, k)
    
    assert sol == expected
 