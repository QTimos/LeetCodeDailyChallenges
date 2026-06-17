class Solution:
    def processStr(self, s: str, k: int) -> str:
        len_of_created_string = 0
        num_of_rems = 0
        num_of_dups = 0
        num_of_flips = 0
        for c in s:
            if ord(c) >= 97 and ord(c) <= 122:
                len_of_created_string += 1
            if c == "*":
                if len_of_created_string > 0:
                    len_of_created_string -= 1
                num_of_rems += 1
            elif c == '#':
                len_of_created_string *= 2
                num_of_dups += 1
            elif c == '%':
                num_of_flips += 1
        if k >= len_of_created_string:
            return "."
        for c in s[::-1]:
            if ord(c) >= 97 and ord(c) <= 122:
                if len_of_created_string - 1 == k:
                    return c
                len_of_created_string -= 1
            if c == "*":
                len_of_created_string += 1
            elif c == '#':
                len_of_created_string //= 2
                k %= len_of_created_string
            elif c == '%':
                k = int((len_of_created_string - 1) - k)
        return s[k] if k < len(s) else "."


def main() -> None:
    s = Solution()
    print(s.processStr("da*ls%kkk#", 5))


if __name__ == "__main__":
    main()
