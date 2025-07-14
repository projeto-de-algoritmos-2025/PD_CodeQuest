class Solution:
    def isMatch(self, s, p):
        # dp[i][j] será True se os primeiros i caracteres de s
        # corresponderem aos primeiros j caracteres de p.
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Caso base: uma string vazia e um padrão vazio correspondem.
        dp[0][0] = True

        # Lida com padrões como a*, a*b*, etc., que podem corresponder a uma string vazia.
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Preenche a tabela de programação dinâmica.
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # Se o caractere do padrão for '.' ou corresponder ao caractere da string.
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Caso 1: O '*' representa zero ocorrências do elemento anterior.                    
                    dp[i][j] = dp[i][j - 2]
                    
                    # Caso 2: O '*' representa uma ou mais ocorrências do elemento anterior.
                    # Verifica se o caractere atual de s corresponde ao caractere ANTES do '*'.
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = False
        
        return dp[len(s)][len(p)]