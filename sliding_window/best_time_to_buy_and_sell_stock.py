"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

def find_best_time_trade_stock(prices):

    """
    Use two pointers
    Left pointer on day 1 (buy)
    Right pointer on day 2 (sell)
    Calculate profit with that window
    If right is less than left, slide pointers right
    Calculate profit with that window
    etc. 

    Time: O(n)
    Space: O(1)
    """
    max_profit = 0
    left_ptr = 0 # Day to buy
    # right_ptr = left_ptr + 1 # Day to sell

    for right_ptr in range(1, len(prices)):
        
        if prices[left_ptr] > prices[right_ptr]:
            left_ptr += 1
            continue
        
        # Calculate current profit and compare to max
        curr_profit = prices[right_ptr] - prices[left_ptr]
        if curr_profit > max_profit:
            max_profit = curr_profit

    return max_profit
        
def test_find_best_time_trade_stock_with_profit():
    prices = [7,1,5,3,6,4]
    expected = 5
    sol = find_best_time_trade_stock(prices)
    assert sol == expected

def test_find_best_time_trade_stock_without_profit():
    prices = [7,6,4,3,1]
    expected = 0 
    sol = find_best_time_trade_stock(prices)
    assert sol == expected

