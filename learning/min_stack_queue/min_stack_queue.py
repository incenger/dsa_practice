from abc import ABCMeta, abstractmethod
from collections import deque


class MinDS(metaclass=ABCMeta):
    """
    An abstract data structure that supports three methods:
    - Add an element
    - Remove and element
    - Find the minimum element
    """

    @abstractmethod
    def add(self, x):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def minimum(self):
        pass


class MinStack(MinDS):
    "Minimum stack"

    def __init__(self):
        self.stack = []

    def add(self, x):
        new_min = x if not self.stack else min(x, self.stack[-1][1])
        self.stack.append((x, new_min))

    def remove(self):
        if self.stack:
            self.stack.pop()

    def minimum(self):
        if not self.stack:
            return None
        return self.stack[-1][1]


class MinQueue(MinDS):
    """
    Minimum queue
    """

    def __init__(self):
        self.queue = deque()
        self.added_cnt = 0
        self.removed_cnt = 0

    def add(self, x):
        while self.queue and self.queue[-1][0] > x:
            self.queue.pop()

        self.queue.append((x, self.added_cnt))
        self.added_cnt += 1

    def remove(self):

        if self.queue and self.queue[0][1] == self.removed_cnt:
            self.queue.popleft()

        self.removed_cnt += 1

    def minimum(self):

        if not self.queue:
            return None

        return self.queue[0][0]


class MinQueue2Stack(MinDS):
    """
    Fully functional min queue implemeted using two min stack
    """

    def __init__(self):
        self.add_stack = []
        self.remove_stack = []

    def add(self, x):
        new_min = x if not self.add_stack else min(x, self.add_stack[-1][1])
        self.add_stack.append((x, new_min))

    def remove(self):

        if not self.remove_stack:
            # Move elements from the add stack to remove stack
            while self.add_stack:
                element = self.add_stack[-1][0]
                self.add_stack.pop()

                min_value = (
                    element
                    if not self.remove_stack
                    else min(element, self.remove_stack[-1][1])
                )

                self.remove_stack.append((element, min_value))

        self.remove_stack.pop()

    def minimum(self):
        min_value = float("inf")
        for s in [self.add_stack, self.remove_stack]:
            min_value = min(min_value, float("inf") if not s else s[-1][1])

        return None if min_value == float("inf") else min_value
