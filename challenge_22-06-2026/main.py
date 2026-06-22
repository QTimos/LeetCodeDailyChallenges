class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        st = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for c in text:
            if c in st:
                st[c] += 1
        st["l"] //= 2
        st["o"] //= 2
        print(st)
        return min(list(st.values()))


def main() -> None:
    s = Solution()
    txt = "loonbalxballpoon"
    print(s.maxNumberOfBalloons(txt))


if __name__ == "__main__":
    main()
