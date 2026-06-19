from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        alts = []
        alts.append(alt)
        for n in gain:
            alt += n
            alts.append(alt)
        return max(alts)

def main() -> None:
    s = Solution()
    print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))


if __name__ == "__main__":
    main()
