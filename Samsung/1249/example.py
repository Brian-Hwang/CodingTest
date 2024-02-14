from heapq import heappush, heappop


def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])
    # Directions: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Initialize distances array with infinity
    distances = [[float("inf")] * cols for _ in range(rows)]
    # Starting point distance is the depth of the starting cell
    distances[0][0] = grid[0][0]
    # Priority queue for Dijkstra's algorithm: (repair time, row, col)
    queue = [(grid[0][0], 0, 0)]

    while queue:
        current_dist, row, col = heappop(queue)
        # If we reach the destination
        if row == rows - 1 and col == cols - 1:
            return current_dist
        for d_row, d_col in directions:
            next_row, next_col = row + d_row, col + d_col
            # Check if next position is within the grid bounds
            if 0 <= next_row < rows and 0 <= next_col < cols:
                # Calculate new distance
                new_dist = current_dist + grid[next_row][next_col]
                # If new distance is shorter, update and push to the queue
                if new_dist < distances[next_row][next_col]:
                    distances[next_row][next_col] = new_dist
                    heappush(queue, (new_dist, next_row, next_col))
    return -1


# Example map (2D array)
# 0 represents the starting and destination points, assumed to be non-damaged for simplicity
example_map = [
    [0, 2, 2, 1],  # S -> Start
    [3, 1, 1, 2],
    [1, 2, 2, 1],
    [2, 1, 1, 0],  # G -> Destination
]

# Calculate the minimum repair time
min_repair_time = dijkstra(example_map)
min_repair_time
