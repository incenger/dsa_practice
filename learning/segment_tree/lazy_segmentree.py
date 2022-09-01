import random

class LazySegmentTreeAddMin:
    def __init__(self, arr):
        self.arr = arr
        self.N = len(arr)

        self.tree = [float("inf")] * self.N * 4
        self.lazy = [0] * self.N * 4
        self._build(1, 0, self.N - 1)

    def _build(self, node_idx, tl, tr):
        """

        Args:
            node_idx: index of the current node in the `self.tree` array
            tl, tr: segment boundaries of the current node
        """
        if tl == tr:
            # Leaf node
            self.tree[node_idx] = self.arr[tl]
        else:
            tm = (tl + tr) // 2
            left_child_idx = 2 * node_idx
            right_child_idx = 2 * node_idx + 1
            self._build(left_child_idx, tl, tm)
            self._build(right_child_idx, tm + 1, tr)

            # Merge siblings
            self.tree[node_idx] = min(
                self.tree[left_child_idx], self.tree[right_child_idx]
            )

    def propagate(self, node_idx, tl, tr):
        """Propagate the changes in the current node to its children."""
        print("Propagate", node_idx, tl, tr)
        left_child_idx = node_idx * 2
        right_child_idx = node_idx * 2 + 1

        self.tree[left_child_idx] += self.lazy[node_idx]
        self.tree[right_child_idx] += self.lazy[node_idx]

        self.lazy[left_child_idx] += self.lazy[node_idx]
        self.lazy[right_child_idx] += self.lazy[node_idx]
        self.lazy[node_idx] = 0

    def update_range(self, node_idx, tl, tr, l, r, inc):
        """
        Increase all elements in the range [l..r] by `inc`.
        """
        print("Update range", node_idx, tl, tr, l, r, inc)

        if l > r:
            return

        if l == tl and tr == r:
            # If the range of this node is the same as range we need to update
            # We will update the value of the current node and its lazy value to propagate later
            self.tree[node_idx] += inc
            self.lazy[node_idx] += inc
        else:
            # Every time we visit a node, we will try to propagate it.
            self.propagate(node_idx, tl, tr)
            tm = (tl + tr) // 2
            self.update_range(node_idx * 2, tl, tm, l, min(tm, r), inc)
            self.update_range(node_idx * 2 + 1, tm + 1, tr, max(l, tm + 1), r, inc)

            self.tree[node_idx] = min(
                self.tree[node_idx * 2], self.tree[node_idx * 2 + 1]
            )

    def query(self, node_idx, tl, tr, l, r):
        """
        Query for the max value in the range [l..r]
        """
        if l > r:
            return -float("inf")

        if l <= tl <= tr <= r:
            return self.tree[node_idx]

        # Every time we visit a node, we will try to propagate it.
        self.propagate(node_idx, tl, tr)
        tm = (tl + tr) // 2

        return max(
            self.query(node_idx * 2, tl, tm, l, min(r, tm)),
            self.query(node_idx * 2, tm + 1, tr, max(l, tm + 1), r),
        )

    def __repr__(self) -> str:
        repr_str = "Arr: " + str(self.arr) + "\n"
        repr_str += "Tree: " + str(self.tree) + "\n"
        repr_str += "Lazy: " + str(self.lazy) + "\n"
        return repr_str


class LazySegmentTreeAddSum:
    def __init__(self, arr):
        self.arr = arr
        self.N = len(arr)

        self.tree = [0] * self.N * 4
        self.lazy = [0] * self.N * 4
        self._build(1, 0, self.N - 1)

    def _build(self, node_idx, tl, tr):
        """

        Args:
            node_idx: index of the current node in the `self.tree` array
            tl, tr: segment boundaries of the current node
        """
        if tl == tr:
            # Leaf node
            self.tree[node_idx] = self.arr[tl]
        else:
            tm = (tl + tr) // 2
            left_child_idx = 2 * node_idx
            right_child_idx = 2 * node_idx + 1
            self._build(left_child_idx, tl, tm)
            self._build(right_child_idx, tm + 1, tr)

            # Merge siblings
            self.tree[node_idx] = self.tree[left_child_idx] + self.tree[right_child_idx]

    def propagate(self, node_idx, tl, tr):
        """Propagate the changes in the current node to its children."""
        # print("Propagate", node_idx, tl, tr)
        left_child_idx = node_idx * 2
        right_child_idx = node_idx * 2 + 1
        tm = (tl + tr) // 2

        self.tree[left_child_idx] += self.lazy[node_idx] * (tm - tl + 1)
        self.tree[right_child_idx] += self.lazy[node_idx] * (tr - tm)

        self.lazy[left_child_idx] += self.lazy[node_idx]
        self.lazy[right_child_idx] += self.lazy[node_idx]
        self.lazy[node_idx] = 0

    def update_range(self, node_idx, tl, tr, l, r, inc):
        """
        Increase all elements in the range [l..r] by `inc`.
        """
        # print("Update range", node_idx, tl, tr, l, r, inc)

        if l > r:
            return

        if l == tl and tr == r:
            # If the range of this node is the same as range we need to update
            # We will update the value of the current node and its lazy value to propagate later
            self.tree[node_idx] += inc * (tr - tl + 1)
            self.lazy[node_idx] += inc
        else:
            # Every time we visit a node, we will try to propagate it.
            self.propagate(node_idx, tl, tr)
            tm = (tl + tr) // 2
            self.update_range(node_idx * 2, tl, tm, l, min(tm, r), inc)
            self.update_range(node_idx * 2 + 1, tm + 1, tr, max(l, tm + 1), r, inc)

            self.tree[node_idx] = self.tree[node_idx * 2] + self.tree[node_idx * 2 + 1]

    def query(self, node_idx, tl, tr, l, r):
        """
        Query for the max value in the range [l..r]
        """
        if l > r:
            return 0 

        if l <= tl <= tr <= r:
            return self.tree[node_idx]

        # Every time we visit a node, we will try to propagate it.
        self.propagate(node_idx, tl, tr)
        tm = (tl + tr) // 2

        return (
            self.query(node_idx * 2, tl, tm, l, min(r, tm))
            + self.query(node_idx * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        )

    def __repr__(self) -> str:
        repr_str = "Arr: " + str(self.arr) + "\n"
        repr_str += "Tree: " + str(self.tree) + "\n"
        repr_str += "Lazy: " + str(self.lazy) + "\n"
        return repr_str


if __name__ == "__main__":
    arr = [5, -7, 9, 0, -2, 8, 3, 6, 4, 1]
    copy_arr = arr[::]
    segtree = LazySegmentTreeAddSum(arr)

    testcase = 10**5
    for _ in range(testcase):
        l = random.randint(0, len(arr) - 1)
        r = random.randint(l, len(arr) - 1)
        inc = random.randint(-1000, 1000)

        for i in range(l, r+1):
            copy_arr[i] += inc

        segtree.update_range(1, 0, len(arr) - 1, l, r, inc)
        gt = sum(copy_arr[l:r+1])
        segtree_return = segtree.query(1, 0, len(arr) - 1, l, r)

        if gt != segtree_return:
            print("Failed")
            break
        # print(gt, segtree_return)






