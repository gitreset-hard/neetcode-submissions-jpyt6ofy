class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        # brute force, just go backwards until next greater day
        span = 0
        for i in range(len(self.prices)-1,-1,-1):
            if self.prices[i] <= price:
                span += 1
            else:
                return span
        
        return span





# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)