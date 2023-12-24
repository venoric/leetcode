class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # compare values and buy on a day when value is less than previous value (pointers)
        # left pointer buy , right pointer sell
        # pointer advances if L > R
        # start with value 0 so it wont automaticaly buy on 7
        # output is 5 (day 2 to 5)
        # buy on minimum and sell on maximum value day
        # cannot go back to previous

        # left and right pointer
        l, r = 0, 1
        maxP = 0
        # while right pointer is less than the length of the array
        while r < len(prices):
            # if the price of the left pointer is less than the right pointer (2 , 5)
            # this means there is a profit so mark that
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # we need to track the max profit because we are not done, we need to check the other values
                maxP = max(profit,maxP)
            else:
                # left increments / changes to new position
                # can increment l + 1 but better to just replace l position with r position
                l = r
            # need to also increment r
            r += 1
        
        return maxP
