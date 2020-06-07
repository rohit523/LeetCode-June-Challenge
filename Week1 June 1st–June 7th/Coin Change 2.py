class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combination = [0] * (amount+1)
        
        combination[0] = 1
        
        for coin in coins:
            for i in range(1, len(combination)):
                if i >= coin:
                    combination[i] += combination[i-coin]
                    
        return combination[amount]
        