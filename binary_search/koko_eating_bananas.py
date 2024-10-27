"""
Eating Bananas
You are given an integer array piles where piles[i] is the number of bananas in
the ith pile. You are also given an integer h, which represents the number of
hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may
choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h
hours.

Example 1:

Input: piles = [1,4,3,2], h = 9

Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours.
With an eating rate of 1, you would need 10 hours to eat all the bananas
(which exceeds h=9), thus the minimum eating rate is 2.

Example 2:

Input: piles = [25,10,23,4], h = 4

Output: 25
Constraints:

1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000
"""
from math import ceil


def calculate_min_consumption_rate(piles, hours):

    sorted_piles = sorted(piles)
    max_count = sorted_piles[-1]
    rate_options = [x for x in range(1, max_count)]

    result = max_count
    left_ptr = 1
    right_ptr = len(rate_options) - 1

    while left_ptr <= right_ptr:
        k = (left_ptr + right_ptr) // 2
        k_hours = sum([ceil(x/k) for x in piles])

        if k_hours <= hours:
            result = min(k, result)
            right_ptr = k - 1
        else:
            left_ptr = k + 1

    return result

def test_calculate_min_consumption_rate():

    piles = [1,4,3,2]
    h = 9
    expected = 2

    solution = calculate_min_consumption_rate(piles=piles, hours=h)
    assert solution == expected

def test_calculate_min_consumption_rate_min_is_max_int():

    piles = [25,10,23,4]
    h = 4
    expected = 25

    solution = calculate_min_consumption_rate(piles=piles, hours=h)
    assert solution == expected
