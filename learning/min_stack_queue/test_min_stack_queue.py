import pytest
from min_stack_queue import MinQueue, MinQueue2Stack, MinStack


def test_min_stack():
    min_stack = MinStack()

    min_stack.add(-2)
    min_stack.add(0)
    min_stack.add(-3)

    assert min_stack.minimum() == -3
    min_stack.remove()
    assert min_stack.minimum() == -2


def test_min_queue():
    min_queue = MinQueue()

    min_queue.add(-3)
    min_queue.add(0)
    min_queue.add(-2)

    assert min_queue.minimum() == -3
    min_queue.remove()
    assert min_queue.minimum() == -2


def test_min_queue_2stack():
    min_queue = MinQueue2Stack()

    min_queue.add(-3)
    min_queue.add(0)
    min_queue.add(-2)

    assert min_queue.minimum() == -3
    min_queue.remove()
    assert min_queue.minimum() == -2
