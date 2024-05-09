class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = []
        n = len(prices)
        for i in range(0,n):
            stack = prices[n:i]
            crnt_disc = stack.pop()
            while(stack):
                x = stack.pop()
                if(prices[i] >= x):
                    crnt_disc = x
            prices[i] -= crnt_disc
        return prices




