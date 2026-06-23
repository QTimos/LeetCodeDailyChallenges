#class Solution:
#    def zigZagArrays(self, n: int, l: int, r: int) -> int:
#        prev_up_dir_poss = [0, 1]
#        prev_down_dir_poss = [0, 1]
#        for length in range(2, n+1):
#            up_dir_poss = [0]
#            down_dir_poss = [0]
#            for j in range(1, length+1):
#                up_dir_poss.append(sum(prev_down_dir_poss[k] for k in range(j, length)))
#                down_dir_poss.append(sum(prev_up_dir_poss[k] for k in range(1, j)))
#            prev_up_dir_poss = up_dir_poss
#            prev_down_dir_poss = down_dir_poss
#        poss = 0
#        for i in range(l, r+1):
#            poss += prev_up_dir_poss[i] + prev_down_dir_poss[i]
#        return poss
#
#

#class Solution:
#    def zigZagArrays(self, n: int, l: int, r: int) -> int:
#        m = r - l
#        if n == 1:
#            return m + 1
#        dir_inc = [v for v in range(m + 1)]
#        dir_dec = [m - v for v in range(m + 1)]
#        for length in range(3, n + 1):
#            new_inc = [0] * (m + 1)
#            new_dec = [0] * (m + 1)
#            current_sum = 0
#            for v in range(m + 1):
#                new_inc[v] = current_sum
#                current_sum = (current_sum + dir_dec[v])
#            current_sum = 0
#            for v in range(m, -1, -1):
#                new_dec[v] = current_sum
#                current_sum = (current_sum + dir_inc[v])
#            dir_inc = new_inc
#            dir_dec = new_dec
#        return (sum(dir_inc) + sum(dir_dec))

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l
        if n == 1:
            return m + 1
        dir_inc = [v for v in range(m + 1)]
        dir_dec = [m - v for v in range(m + 1)]
        for length in range(3, n + 1):
            new_inc = [0] * (m + 1)
            new_dec = [0] * (m + 1)
            current_sum = 0
            for v in range(m + 1):
                new_inc[v] = current_sum
                current_sum = (current_sum + dir_dec[v]) % MOD
            current_sum = 0
            for v in range(m, -1, -1):
                new_dec[v] = current_sum
                current_sum = (current_sum + dir_inc[v]) % MOD
            dir_inc = new_inc
            dir_dec = new_dec
        return (sum(dir_inc) + sum(dir_dec)) % MOD


def main() -> None:
    s = Solution()
    print(s.zigZagArrays(3, 1, 3))


if __name__ == "__main__":
    main()


