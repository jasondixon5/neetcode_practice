"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
integer.

You must write an algorithm that runs in O(n) time and without using the 
division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output
array does not count as extra space for space complexity analysis.)

"""

def product_except_self_prefix_postfix_approach(nums):

    output = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        output[i] = (prefix)
        prefix = nums[i] * prefix

    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] = output[i] * postfix
        postfix = nums[i] * postfix

    return output

def test_product_except_self_prefix_postfix_approach():

    inputs = {
        tuple([1,2,3,4]): [24,12,8,6],
        tuple([-1,1,0,-3,3]): [0,0,9,0,0],
    }

    for input, expected in inputs.items():

        sol = product_except_self_prefix_postfix_approach(input)
        
        assert sol == expected


# def _manual_test_ri():

#     input = [1,2,3,4]
#     expected = [24,12,8,6]

#     pre, post, output = ri_product_except_self_reduced_space(input)

#     print(f"""
#         Input: {input}
#         Prefix: {pre}
#         Postfix: {post}
#         Output: {output}
#         Expected: {expected}
        
#     """)

#     input = [-1,1,0,-3,3]
#     expected = [0,0,9,0,0]

#     pre, post, output = ri_product_except_self(input)

#     print(f"""
#         Input: {input}
#         Prefix: {pre}
#         Postfix: {post}
#         Output: {output}
#         Expected: {expected}
        
#     """)

# if __name__ == "__main__":
#     _manual_test_ri()
