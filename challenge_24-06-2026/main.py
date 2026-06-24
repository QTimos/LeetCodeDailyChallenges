class Solution:
    def multiply(self, A, B, MOD):
        B_cols = list(zip(*B))
        return [
                [
                    sum(a * b for a, b in zip(A_row, B_col))%MOD
                    for B_col in B_cols
                    ]
                    for A_row in A
                ]

    def matrix_exponentiation(self, M, power, MOD):
        m = len(M)
        res = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
        base = M
        while power > 0:
            if power % 2 == 1:
                res = self.multiply(res, base, MOD)
            base = self.multiply(base, base, MOD)
            power //= 2
        return res

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD =  10**9 + 7
        m = r - l + 1
        L = [[1 if c > r else 0 for c in range(m)] for r in range(m)]
        U = [[1 if c < r else 0 for c in range(m)] for r in range(m)]
        UL = self.multiply(U, L, MOD)
        n_0 = (n - 1) // 2
        T = self.matrix_exponentiation(UL, n_0, MOD)
        if (n - 1) % 2 != 0:
            T = self.multiply(L, T, MOD)
        X = [1] * m
        FX = [0] * m
        for r in range(m):
            for c in range(m):
                FX[r] = (FX[r] + T[r][c] * X[c]) % MOD
        return (sum(FX)*2) % MOD


def main() -> None:
    s = Solution()
    print(s.zigZagArrays(3, 1, 3))


if __name__ == "__main__":
    main()
