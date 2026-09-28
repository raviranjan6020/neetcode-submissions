class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left is best day to buy
        # right is best day to sell
        # if prices[right] > prices[left] then we can sell
        # else prices[right] < prices[left] then right is our new beast day yto buy
        # record maximum profit at end of each
        left,profit=0,0
        for right in range(len(prices)):
            if prices[right] > prices[left]:
                profit=max(profit, prices[right]-prices[left])
            else:
                left=right
        return profit

        