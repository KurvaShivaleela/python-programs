16
#shortest
import heapq

class Solution:
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])

        # Correct 2D distance matrix
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        # Min heap: (effort, row, col)
        heap = [(0, 0, 0)]

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while heap:
            effort, r, c = heapq.heappop(heap)

            # If reached destination
            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(effort, diff)

                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))

        return 0


# ---- Main program ----
if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    heights = []
    print("Enter the matrix row by row:")
    for _ in range(m):
        heights.append(list(map(int, input().split())))

    obj = Solution()
    print("Output:", obj.minimumEffortPath(heights))