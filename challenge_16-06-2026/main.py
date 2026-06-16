class Solution:
    def processStr(self, s: str) -> str:
        new_str = ""
        for c in s:
            if ord(c) >= 97 and ord(c) <= 122:
                new_str += c
            elif c == '*':
                new_str = new_str[0:-1]
            elif c == '#':
                new_str += new_str
            elif c == '%':
                new_str = new_str[::-1]
            else:
                continue
        return new_str

def main() -> None:
    solution = Solution()


if __name__ == "__main__":
    main()
