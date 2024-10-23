"""
Search 2D Matrix
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous
row.

Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
   1    2    4    8
  10   11   12   13
  14   20   30   40
  Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

  Output: true

Example 2:

     1    2    4    8
    10   11   12   13
    14   20   30   40

   Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

   Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000

"""

def binary_search_2d_matrix(matrix, target):

    left_outer_list_pointer = 0
    right_outer_list_pointer = len(matrix) - 1

    while left_outer_list_pointer <= right_outer_list_pointer:
        midpoint_outer_list = (left_outer_list_pointer + right_outer_list_pointer) // 2

        submatrix = matrix[midpoint_outer_list]

        if submatrix[0] > target:
            right_outer_list_pointer = midpoint_outer_list - 1
        elif submatrix[len(submatrix) - 1] < target:
            left_outer_list_pointer = midpoint_outer_list + 1
        else:
            return binary_search_1d_list(submatrix, target)

def binary_search_1d_list(nums, target):

    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer <= right_pointer:
        midpoint = (left_pointer + right_pointer) // 2

        if nums[midpoint] == target:
            return True
        elif nums[midpoint] > target:
            right_pointer = midpoint - 1
        else:
            left_pointer = midpoint + 1

    return False

def test_binary_search_2d_matrix_target_in_middle_sublist():

    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 10
    expected = True

    solution = binary_search_2d_matrix(matrix, target)
    assert solution == expected

def test_binary_search_2d_matrix_target_not_in_matrix():

    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 15
    expected = False

    solution = binary_search_2d_matrix(matrix, target)
    assert solution == expected

def test_binary_search_2d_matrix_target_near_end_of_last_list():

    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 30
    expected = True

    solution = binary_search_2d_matrix(matrix, target)
    assert solution == expected
