# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
class Solution1:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_sp = prices[0]
        for i in range(0, len(prices)):
            min_sp = min(prices[i], min_sp)
            max_profit = max(prices[i] - min_sp, max_profit)
        return max_profit

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        l = 0
        for r in range(1,len(prices)):
            # print("l={}, r={}".format(l, r))
            if prices[r] < prices[l]:
                l=r
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        return max_profit


s = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
prices2 =[2,4,1]
print("max profit=", s.maxProfit(prices2))
