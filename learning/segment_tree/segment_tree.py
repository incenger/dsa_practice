class SimpleSegmentTree:
    def __init__(self, arr, merge_op, null_value):
        self.arr = arr
        self.merge_op = merge_op
        self.null_value = null_value

        self.N = len(self.arr)
        self.tree = [None] * self.N * 4  # The max size of the tree is 4N
        self._build(1, 0, self.N - 1)

    def update(self, pos, val):
        self._update(1, 0, self.N - 1, pos, val)

    def query(self, l, r):
        return self._query(1, 0, self.N - 1, l, r)

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
            self.tree[node_idx] = self.merge_op(
                self.tree[left_child_idx], self.tree[right_child_idx]
            )

    def _query(self, node_idx, tl, tr, ql, qr):
        """

        Args:
            node_idx: index of the current node in the `self.tree` array
            tl, tr: segment boundaries of the current node
            ql, qr: boundaries of the query segment
        """

        if ql > qr:
            return self.null_value

        if ql <= tl <= tr <= qr:
            return self.tree[node_idx]

        tm = (tl + tr) // 2
        left_result = self._query(node_idx * 2, tl, tm, ql, min(qr, tm))
        right_result = self._query(node_idx * 2 + 1, tm + 1, tr, max(ql, tm + 1), qr)
        return self.merge_op(left_result, right_result)

    def _update(self, node_idx, tl, tr, pos, val):
        """
        Args:
            node_idx: index of the current node in the `self.tree` array
            tl, tr: segment boundaries of the current node
            pos: position in the original array to perform update
            val: the updated value
        """

        if tl == tr:
            # Leaf node, update value
            self.tree[node_idx] = val
            self.arr[pos] = val
        else:
            tm = (tl + tr) // 2
            left_child_idx = 2 * node_idx
            right_child_idx = 2 * node_idx + 1

            if pos <= tm:
                self._update(left_child_idx, tl, tm, pos, val)
            else:
                self._update(right_child_idx, tm + 1, tr, pos, val)

            self.tree[node_idx] = self.merge_op(
                self.tree[left_child_idx], self.tree[right_child_idx]
            )


# TODO: This code has better runtime in Python, Check this out
class EfficientSegmentTree:
    def __init__(self, arr, merge_op, null_value):
        self.n = len(arr)
        self.merge_op = merge_op
        self.null_value = null_value

        # All the leaves start from index `n`-th
        self.tree = [0] * self.n + arr
        self._build()

    def _build(self):
        for i in range(self.n - 1, -1, -1):
            self.tree[i] = self.merge_op(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        # [l, r)

        # Go to the corresponding leaves node
        l += self.n
        r += self.n

        ans = self.null_value

        while l < r:
            if l & 1:
                # If l is odd, it's a right children of its parent
                # This means the query range won't cover the parent of l
                # We take the value of node at l and move to the right of l's parent
                # l = (l + 1) // 2 (//2 later)
                # Otherwise if l is even, then we move to the parent of l
                # l = l//2
                ans = self.merge_op(ans, self.tree[l])
                l += 1
            if r & 1:
                # Similar to l, but we need to decrease r first because the r end is excluded
                r -= 1
                ans = self.merge_op(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.merge_op(self.tree[i * 2], self.tree[i * 2 + 1])

    def get(self, i):
        return self.tree[i + self.n]
