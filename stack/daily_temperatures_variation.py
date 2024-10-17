"""
Daily Temperatures
You are given an array of integers temperatures where temperatures[i] represents
the daily temperatures on the ith day.

Return an array result where result[i] is the number of days before the ith day
that have been warmer than the ith day.

If there is no day in the past where a warmer temp occurred, set result[i] to 0.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]
Output: [0, 0, 1, 2, 1, 0, 2]

Example 2:

Input: temperatures = [20,21,22]
Output: [0,0,0]

Constraints:

1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100
"""

def calculate_warming_intervals(temps):
	
	result = []
	stack = []

	return result

def test_calculate_warming_intervals_standard():
	temperatures = [30,38,30,36,35,40,28]
	expected = [0, 0, 1, 2, 1, 0, 2]
	solution = calculate_warming_intervals(temperatures)

	assert solution == expected

def test_calculate_warming_intervals_no_warming():
	temperatures = [20,21,22]
	expected = [0,0,0]
	solution = calculate_warming_intervals(temperatures)

	assert solution == expected

