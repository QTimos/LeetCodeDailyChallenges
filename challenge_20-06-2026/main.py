from typing import List
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        if not any(r[0] == n for r in restrictions):
            restrictions.append([n, n-1])
        restrictions.sort()
        i = 0
        while i < len(restrictions):
            if i+1 < len(restrictions) and restrictions[i+1][1] > restrictions[i][1] + abs(restrictions[i+1][0] - restrictions[i][0]):
                restrictions[i+1][1] = restrictions[i][1] + abs(restrictions[i+1][0] - restrictions[i][0])
            i += 1
        i = len(restrictions) - 1
        while i >= 0:
            if i-1 >= 0 and restrictions[i-1][1] > restrictions[i][1] + abs(restrictions[i-1][0] - restrictions[i][0]):
                restrictions[i-1][1] = restrictions[i][1] + abs(restrictions[i-1][0] - restrictions[i][0])
            i -= 1
        max_height = 0
        for i in range(len(restrictions) - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
        return max_height



s = Solution()
lis = [[8,5],[9,0],[6,2],[4,0],[3,2],[10,0],[5,3],[7,3],[2,4]]
#print(lis)
print(s.maxBuilding(10, lis))
