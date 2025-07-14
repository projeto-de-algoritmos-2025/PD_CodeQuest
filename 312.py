class Solution:
    def maxCoins(self, nums):
        # Adiciona balões virtuais com valor 1 nas bordas
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j] armazena o máximo de moedas ao estourar balões no intervalo (i, j)
        dp = [[0] * n for _ in range(n)]

        # último balão a ser estourado em um intervalo [left, right].
        # Se o balão 'k' é o último a ser estourado, então todos os balões em (left, k) e (k, right) já foram estourados.
        for length in range(2, n):  # Comprimento do intervalo
            for left in range(n - length):
                right = left + length
                # 'k' é o último balão a ser estourado no intervalo (left, right)
                for k in range(left + 1, right):
                    coins = nums[left] * nums[k] * nums[right]
                    total = coins + dp[left][k] + dp[k][right]
                    dp[left][right] = max(dp[left][right], total)

        return dp[0][n - 1]