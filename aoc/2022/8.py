def part_1():

    # O(MN) solution

    with open('input.txt', 'r') as f:
        forest = [l.strip() for l in f.readlines()]

    (m, n) = (len(forest), len(forest[0]))

    def check_visible(trees):
        visible = [False] * len(trees)
        block_height = trees[0]
        for i in range(len(trees)):
            if i == 0 or trees[i] > block_height:
                visible[i] = True
            block_height = max(block_height, trees[i])
        return visible

    is_visible_row = []
    for tree_row in forest:
        visible_from_left = check_visible(tree_row)
        visible_from_right = check_visible(tree_row[::-1])
        is_visible_row.append([l or r for (l, r) in
                              zip(visible_from_left,
                              reversed(visible_from_right))])

    is_visible_col = []
    for j in range(n):
        tree_col = ''.join(forest[i][j] for i in range(m))
        visible_from_top = check_visible(tree_col)
        visible_from_bottom = check_visible(tree_col[::-1])
        is_visible_col.append([t or b for (t, b) in
                              zip(visible_from_top,
                              reversed(visible_from_bottom))])

    num_visible = 0
    for i in range(m):
        for j in range(n):
            if is_visible_row[i][j] or is_visible_col[j][i]:
                num_visible += 1
    print ('Part 1', num_visible)


def part_2():

    # O(MN)

    with open('input.txt', 'r') as f:
        forest = [l.strip() for l in f.readlines()]

    (m, n) = (len(forest), len(forest[0]))
    viewing_distance = [[1] * n for _ in range(m)]

    def compute_view_distance(trees):
        stack = []

        viewing_distance = []
        for i in range(len(trees)):
            while stack and trees[i] > trees[stack[-1]]:
                stack.pop()

            if not stack:
                viewing_distance.append(i)
            else:
                viewing_distance.append(i - stack[-1])
            stack.append(i)
        return viewing_distance

    row_viewing_distance = []
    for tree_row in forest:
        visible_from_left = compute_view_distance(tree_row)
        visible_from_right = compute_view_distance(tree_row[::-1])
        row_viewing_distance.append([l * r for (l, r) in
                                    zip(visible_from_left,
                                    reversed(visible_from_right))])

    col_viewing_distance = []
    for j in range(n):
        tree_col = ''.join(forest[i][j] for i in range(m))
        visible_from_top = compute_view_distance(tree_col)
        visible_from_bottom = compute_view_distance(tree_col[::-1])
        col_viewing_distance.append([t * b for (t, b) in
                                    zip(visible_from_top,
                                    reversed(visible_from_bottom))])

    max_viewing_distance = 0
    for i in range(m):
        for j in range(n):
            max_viewing_distance = max(max_viewing_distance,
                    row_viewing_distance[i][j]
                    * col_viewing_distance[j][i])
    print ('Part 2', max_viewing_distance)


if __name__ == '__main__':
    part_1()
    part_2()
