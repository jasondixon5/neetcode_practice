"""
Daily Temperatures
You are given an array of integers temperatures where temperatures[i] represents
the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day 
before a warmer temperature appears on a future day. If there is no day in the 
future where a warmer temperature will appear for the ith day, set result[i] to 
0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:

1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100
"""
def calculate_warming_intervals(temps):

	stack = [] # Will hold pairs of format [index, temperature]
	result = [0] * len(temps)

	for i in range(len(temps)):

		while stack and temps[i] > stack[-1][1]:

			idx, temp = stack.pop()
			result[idx] = i - idx #calc'ing distnc *from* earlier val so store at idx for that val

		stack.append([i, temps[i]])

	return result

def test_calculate_warming_intervals():

    temps = [30,38,30,36,35,40,28]
    expected = [1,4,1,2,1,0,0]
    output = calculate_warming_intervals(temps)

    assert output == expected

def test_calculate_warming_intervals_no_warmer_days():
    temps = [22,21,20]
    expected = [0,0,0]
    output = calculate_warming_intervals(temps)

    assert output == expected

