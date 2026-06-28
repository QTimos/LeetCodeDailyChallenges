class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        hm = {}
        for n in nums:
            v = hm.get(n, 0)
            hm[n] = v + 1
        max_len = 0
        l = 1
        if 1 in hm:
            for l in hm:
                c1 = hm[1]
                max_len = c1 if c1 % 2 != 0 else c1 -1
        for n in hm:
            if n == 1:
                continue
            curr_len = 0
            x = n
            while x in hm and hm[x] >= 2:
                curr_len += 2
                x = x * x
            if x in hm:
                curr_len += 1
            else:
                curr_len -= 1
            max_len = max(max_len, curr_len)
        return max_len

def main() -> None:
    s = Solution()
    nums = [5, 4, 1, 2, 2]
    print(s.maximumLength(nums))


if __name__ == "__main__":
    main()
