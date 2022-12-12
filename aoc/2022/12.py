def part_1():
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    with open('input.txt', 'r') as f:
        heightmap = [list(map(ord, line.strip())) for line in
                     f.readlines()]

    (m, n) = (len(heightmap), len(heightmap[0]))
    visited = [[False] * n for _ in range(m)]
    current_position = None
    best_signal_position = None

    for i in range(m):
        for j in range(n):
            if heightmap[i][j] == ord('S'):
                current_position = (i, j)
                heightmap[i][j] = ord('a')

            if heightmap[i][j] == ord('E'):
                best_signal_position = (i, j)
                heightmap[i][j] = ord('z')

    queue = [current_position]
    visited[current_position[0]][current_position[1]] = True
    step = 0

    found = False
    while not found and queue:
        new_queue = []
        for (x, y) in queue:
            if (x, y) == best_signal_position:
                found = True
                break

            current_height = heightmap[x][y]

            for (dx, dy) in DIRS:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] \
                    and current_height + 1 >= heightmap[nx][ny]:
                    visited[nx][ny] = True
                    new_queue.append((nx, ny))

        if found:
            break
        queue = new_queue
        step += 1

    assert found
    print ('Part 1', step)


def part_2():
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    with open('input.txt', 'r') as f:
        heightmap = [list(map(ord, line.strip())) for line in
                     f.readlines()]

    (m, n) = (len(heightmap), len(heightmap[0]))
    visited = [[False] * n for _ in range(m)]
    start_position = None

    for i in range(m):
        for j in range(n):
            if heightmap[i][j] == ord('E'):
                start_position = (i, j)
                heightmap[i][j] = ord('z')
            if heightmap[i][j] == ord('S'):
                heightmap[i][j] = ord('a')

    queue = [start_position]
    visited[start_position[0]][start_position[1]] = True
    step = 0

    found = False
    while not found and queue:
        new_queue = []
        for (x, y) in queue:
            current_height = heightmap[x][y]

            if current_height == ord('a'):
                found = True
                break

            for (dx, dy) in DIRS:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] \
                    and current_height <= heightmap[nx][ny] + 1:
                    visited[nx][ny] = True
                    new_queue.append((nx, ny))

        if found:
            break
        queue = new_queue
        step += 1

    assert found
    print ('Part 2', step)


if __name__ == '__main__':
    part_1()
    part_2()
