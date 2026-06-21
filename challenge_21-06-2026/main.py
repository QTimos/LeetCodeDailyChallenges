from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for c in costs:
            if c > coins:
                break
            coins -= c
            count += 1
        return count

def main() -> None:
    s = Solution()
#    costs = [1,3,2,4,1]
#    coins = 7
#    costs = [10,6,8,7,7,8]
#    coins = 5
    costs = [1,6,3,1,2,5]
    coins = 20
    print(s.maxIceCream(costs, coins))


if __name__ == "__main__":
    main()
