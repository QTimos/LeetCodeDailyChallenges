class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        return min(abs((minutes * 6) - (((5 * hour) + (minutes / 12)) * 6)), 360 - abs((minutes * 6) - (((5 * hour) + (minutes / 12)) * 6)))

def main() -> None:
    s = Solution()
    print(s.angleClock(12, 30))

if __name__ == "__main__":
    main()
