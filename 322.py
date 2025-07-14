class Solution:
    def coinChange(self, coins, amount):
        # dp[i] armazenará o número mínimo de moedas para a quantia i.
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # Para cada quantia de 1 até amount
        for i in range(1, amount + 1):
            # Para cada moeda disponível
            for coin in coins:
                # Se a quantia i for maior ou igual à moeda
                if i - coin >= 0:
                    # A nova solução para dp[i] pode ser a atual ou 1 + a solução para (i - coin)
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # Se dp[amount] ainda for infinito, significa que não foi encontrada uma solução.
        if dp[amount] == float('inf'):
            return -1
        else:
            return int(dp[amount])