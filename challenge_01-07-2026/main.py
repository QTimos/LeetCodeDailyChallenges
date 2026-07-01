class Solution:
    from collections import deque
    import heapq
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    queue.append((i, j))
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        pq = [(-dist[0][0], 0, 0)]
        max_sf = [[-1] * n for _ in range(n)]
        max_sf[0][0] = dist[0][0]
        while pq:
            sf, r, c = heapq.heappop(pq)
            sf = -sf
            if r == n - 1 and c == n - 1:
                return sf
            if sf < max_sf[r][c]:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    next_sf = min(sf, dist[nr][nc])
                    if next_sf > max_sf[nr][nc]:
                        max_sf[nr][nc] = next_sf
                        heapq.heappush(pq, (-next_sf, nr, nc))
        return 0


def main() -> None:
    raise NotImplentedError()


if __name__ == "__main__":
    main()
