class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        c = 0
        for p in patterns:
            if p in word:
                c += 1
        return c


def main() -> None:
    s = Solution()
    patterns = ["a","abc","bc","d"]
    word = "abc"
    print(s.numOfStrings(patterns, word))


if __name__ == "__main__":
    main()
