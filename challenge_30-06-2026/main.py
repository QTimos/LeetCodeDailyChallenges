class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hmap = {'a': 0, 'b': 0, 'c': 0}
        c = 0
        l = 0
        n = (len(s))
        for r in range(n):
            hmap[s[r]] += 1
            while hmap['a'] > 0 and hmap['b'] > 0 and hmap['c'] > 0:
                c += n - r
                hmap[s[l]] -= 1
                l += 1
        return c



def main() -> None:
    s = Solution()
    print(s.numberOfSubstrings("aaacb"))


if __name__ == "__main__":
    main()
